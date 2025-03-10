# Copyright 2024 The OpenXLA Authors.
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
# ==============================================================================
"""Utilities for visiting XPlanes."""

from typing import Any, Iterator, Mapping, Optional, Sequence, Tuple


class XSpaceVisitor:
  """Parses a XSpace protobuf and provides accessors to its contents."""

  def __init__(self, serialized_xspace: bytes):
    ...

  @classmethod
  def from_file(cls, path: str) -> 'XSpaceVisitor':
    """Creates an XSpaceVisitor from a serialized XSpace proto file."""
    ...

  @classmethod
  def from_serialized_xspace(cls, serialized_xspace: bytes) -> 'XSpaceVisitor':
    """Creates an XSpaceVisitor from a serialized XSpace proto."""
    ...

  @classmethod
  def from_raw_cpp_ptr(cls, raw_proto_ptr: object) -> 'XSpaceVisitor':
    """Creates an XSpaceVisitor from a raw C++ pointer enclosed in a capsule to a XSpace proto."""
    ...

  @property
  def planes(self) -> Iterator['XPlaneVisitor']:
    ...

  def find_plane_with_name(self, name: str) -> Optional['XPlaneVisitor']:
    """Finds the plane with the given name."""
    ...


class XPlaneVisitor:
  """Wraps XPlane protobuf and provides accessors to its contents."""

  @property
  def name(self) -> str:
    """Name of the plane."""
    ...

  @property
  def lines(self) -> Iterator['XLineVisitor']:
    """Lines in the plane."""
    ...

  @property
  def stats(self) -> Iterator[Tuple[str, Any]]:
    """Stats in the plane.

    Returns
      An iterator of (name, value) tuples, note that for metadata ids that
      are not found, the returned tuple will be (None, None). The caller should
      check the tuple value before using it.
    """
    ...


class XLineVisitor:
  """Wraps XLine protobuf and provides accessors to its contents."""

  @property
  def name(self) -> str:
    """Name of the line."""
    ...

  @property
  def events(self) -> Iterator['XEventVisitor']:
    """Events in the line."""
    ...


class XEventVisitor:
  """Wraps XEvent protobuf and provides accessors to its contents."""

  @property
  def start_ns(self) -> float:
    """Start time of the event in nanoseconds."""
    ...

  @property
  def duration_ns(self) -> float:
    """Duration of the event in nanoseconds."""
    ...

  @property
  def end_ns(self) -> float:
    """End time of the event in nanoseconds."""
    ...

  @property
  def name(self) -> str:
    """Name of the event."""
    ...

  @property
  def stats(self) -> Iterator[Tuple[str, Any]]:
    """Stats of the event.

    Returns
      An iterator of (name, value) tuples, note that for metadata ids that
      are not found, the returned tuple will be (None, None). The caller should
      check the tuple value before using it.
    """
    ...
