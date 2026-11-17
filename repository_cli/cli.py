# SPDX-FileCopyrightText: 2021-2026 Graz University of Technology.
# SPDX-License-Identifier: MIT

"""CLI commands for repository-cli."""

from click import group

from .records import group_records
from .users import group_users


@group()
def utilities() -> None:
    """Utility commands for TU Graz Repository."""


utilities.add_command(group_users)
utilities.add_command(group_records)
