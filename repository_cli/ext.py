# SPDX-FileCopyrightText: 2021-2026 Graz University of Technology.
# SPDX-License-Identifier: MIT

"""CLI utilities for TU Graz Repository."""

from flask import Flask


class RepositoryCli:
    """repository-cli extension."""

    def __init__(self, app: Flask = None) -> None:
        """Extension initialization."""
        if app:
            self.init_app(app)

    def init_app(self, app: Flask) -> None:
        """Flask application initialization."""
        app.extensions["repository-cli"] = self
