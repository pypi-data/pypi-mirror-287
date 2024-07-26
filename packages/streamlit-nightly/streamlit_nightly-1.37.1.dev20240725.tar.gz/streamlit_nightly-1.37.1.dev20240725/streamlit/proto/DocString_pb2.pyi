"""
@generated by mypy-protobuf.  Do not edit manually!
isort:skip_file
*!
Copyright (c) Streamlit Inc. (2018-2022) Snowflake Inc. (2022-2024)

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

    http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.
"""

import builtins
import collections.abc
import google.protobuf.descriptor
import google.protobuf.internal.containers
import google.protobuf.message
import typing

DESCRIPTOR: google.protobuf.descriptor.FileDescriptor

@typing.final
class DocString(google.protobuf.message.Message):
    """Formatted text"""

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    DOC_STRING_FIELD_NUMBER: builtins.int
    TYPE_FIELD_NUMBER: builtins.int
    NAME_FIELD_NUMBER: builtins.int
    VALUE_FIELD_NUMBER: builtins.int
    MEMBERS_FIELD_NUMBER: builtins.int
    doc_string: builtins.str
    """The doc string."""
    type: builtins.str
    """The type of the object."""
    name: builtins.str
    """The name the user gave to the variable holding this object."""
    value: builtins.str
    """A string representation of this object's value."""
    @property
    def members(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[global___Member]:
        """List of this object's methods and member variables."""

    def __init__(
        self,
        *,
        doc_string: builtins.str = ...,
        type: builtins.str = ...,
        name: builtins.str = ...,
        value: builtins.str = ...,
        members: collections.abc.Iterable[global___Member] | None = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing.Literal["doc_string", b"doc_string", "members", b"members", "name", b"name", "type", b"type", "value", b"value"]) -> None: ...

global___DocString = DocString

@typing.final
class Member(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    NAME_FIELD_NUMBER: builtins.int
    TYPE_FIELD_NUMBER: builtins.int
    VALUE_FIELD_NUMBER: builtins.int
    DOC_STRING_FIELD_NUMBER: builtins.int
    name: builtins.str
    """The name of the object."""
    type: builtins.str
    """The type of the object."""
    value: builtins.str
    """A string representation of this member's value."""
    doc_string: builtins.str
    """The doc string."""
    def __init__(
        self,
        *,
        name: builtins.str = ...,
        type: builtins.str = ...,
        value: builtins.str = ...,
        doc_string: builtins.str = ...,
    ) -> None: ...
    def HasField(self, field_name: typing.Literal["contents", b"contents", "doc_string", b"doc_string", "value", b"value"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing.Literal["contents", b"contents", "doc_string", b"doc_string", "name", b"name", "type", b"type", "value", b"value"]) -> None: ...
    def WhichOneof(self, oneof_group: typing.Literal["contents", b"contents"]) -> typing.Literal["value", "doc_string"] | None: ...

global___Member = Member
