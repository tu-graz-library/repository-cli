# SPDX-FileCopyrightText: 2023-2026 Graz University of Technology.
# SPDX-License-Identifier: MIT

"""Types."""

from dataclasses import dataclass


@dataclass(frozen=True)
class Color:
    """The class is for the output color management."""

    neutral = "white"
    error = "red"
    warning = "yellow"
    abort = "magenta"
    success = "green"
    alternate = ("blue", "cyan")
