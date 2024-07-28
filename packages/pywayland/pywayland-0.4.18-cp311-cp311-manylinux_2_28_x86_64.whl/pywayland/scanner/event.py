# Copyright 2015 Sean Vig
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

from __future__ import annotations

import xml.etree.ElementTree as ET
from dataclasses import dataclass
from typing import Iterator

from .argument import Argument, ArgumentType
from .description import Description
from .method import Method
from .printer import Printer


@dataclass(frozen=True)
class Event(Method):
    """Scanner for event objects (server-side method)

    Required attributes: `name`

    Optional attributes: `since`

    Child elements: `description` and `arg``
    """

    method_type = "event"

    @classmethod
    def parse(cls, element: ET.Element) -> Event:
        name = cls.parse_attribute(element, "name")
        if name in ("global", "import"):
            name += "_"

        return cls(
            name=name,
            since=cls.parse_optional_attribute(element, "since"),
            description=cls.parse_optional_child(element, Description, "description"),
            arg=cls.parse_repeated_child(element, Argument, "arg"),
        )

    @property
    def method_args(self) -> Iterator[str]:
        """Generator of the arguments to the method

        All arguments to be sent to `._post_event` must be passed in
        """
        for arg in self.arg:
            yield arg.signature

    def output_doc_params(self, printer: Printer) -> None:
        """Aguments documented as parameters

        All arguments are event parameters.
        """
        for arg in self.arg:
            arg.output_doc_param(printer)

    def output_body(self, printer: Printer, opcode: int) -> None:
        """Output the body of the event to the printer"""
        args = ", ".join([str(opcode)] + [arg.name for arg in self.arg])
        printer(f"self._post_event({args})")

    @property
    def return_type(self) -> str:
        return "None"

    @property
    def needs_any(self) -> bool:
        for arg in self.arg:
            if (
                arg.type in (ArgumentType.Object, ArgumentType.NewId)
                and not arg.interface
            ):
                return True
        return False
