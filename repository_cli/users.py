# SPDX-FileCopyrightText: 2021-2026 Graz University of Technology.
# SPDX-License-Identifier: MIT

"""Management commands for users."""

from click import group
from flask.cli import with_appcontext
from invenio_accounts.models import User
from tabulate import tabulate


@group("users")
def group_users() -> None:
    """Management commands for users."""


@group_users.command("list")
@with_appcontext
def list_users() -> None:
    """List registered users.

    example call:
        invenio repository users list
    """
    users = []

    for user in User.query:
        active = "YES" if user.active else "NO"

        users.append([user.id, user.email, active, user.confirmed_at])

    print(tabulate(users, headers=["id", "email", "active", "confirmed"]))  # noqa: T201
