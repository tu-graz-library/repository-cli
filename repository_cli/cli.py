# -*- coding: utf-8 -*-
#
# Copyright (C) 2021-2023 Graz University of Technology.
#
# repository-cli is free software; you can redistribute it and/or modify it
# under the terms of the MIT License; see LICENSE file for more details.

"""CLI commands for repository-cli."""

from click import group

from .records import group_records
from .users import group_users


@group()
def utilities() -> None:
    """Utility commands for TU Graz Repository."""


utilities.add_command(group_users)
utilities.add_command(group_records)
