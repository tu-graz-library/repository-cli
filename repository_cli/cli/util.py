# -*- coding: utf-8 -*-
#
# Copyright (C) 2021 Graz University of Technology.
#
# repository-cli is free software; you can redistribute it and/or modify it
# under the terms of the MIT License; see LICENSE file for more details.

"""Commonly used utility functions."""

from flask_principal import Identity
from invenio_access.permissions import any_user, system_process


def get_identity(permission_name="any_user"):
    """Get an identity to perform tasks.

    Default is "any_user"
    """
    identity = Identity(0)
    permission = any_user
    if permission_name == "system_process":
        permission = system_process

    identity.provides.add(permission)  # system_process permissions
    return identity
