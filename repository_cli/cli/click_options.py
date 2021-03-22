# -*- coding: utf-8 -*-
#
# Copyright (C) 2021 Graz University of Technology.
#
# repository-cli is free software; you can redistribute it and/or modify it
# under the terms of the MIT License; see LICENSE file for more details.

"""Commonly used options for CLI commands."""

import click

option_identifier = click.option(
    "--identifier",
    "-i",
    required=True,
    help="metadata identifier as JSON",
)

option_pid = click.option(
    "--pid",
    "-p",
    metavar="PID_VALUE",
    required=True,
    help="persistent identifier of the object to operate on",
)

# invenio repository records identifiers list -p "fcze8-4vx33"
# invenio repository records identifiers add -p "fcze8-4vx33" -i "data"
