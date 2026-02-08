# -*- coding: utf-8 -*-
#
# Copyright (C) 2026 Graz University of Technology.
#
# repository-cli is free software; you can redistribute it and/or modify it
# under the terms of the MIT License; see LICENSE file for more details.

"""Mock module."""

from flask import Blueprint, Flask


def create_invenio_app_rdm_records_blueprint(app: Flask) -> Blueprint:
    """Create fake invenio_app_rdm_records Blueprint akin to invenio-app-rdm's."""
    blueprint = Blueprint(
        "invenio_app_rdm_records",
        __name__,
    )

    @blueprint.route("/records/<pid_value>/files/<path:filename>")
    def record_file_download(*_: tuple, **__: dict) -> str:
        """Fake record_file_download view function."""
        return "<file content>"

    @blueprint.route("/uploads/<pid_value>")
    def deposit_edit(*_: tuple, **__: dict) -> str:
        """Fake record_detail view function."""
        return "<deposit edit>"

    @blueprint.route("/records/<pid_value>")
    def record_detail(*_: tuple, **__: dict) -> str:
        """Fake record_detail view function."""
        return "<record detail>"

    @blueprint.route("/records/<pid_value>/latest")
    def record_latest(*_: tuple, **__: dict) -> str:
        """Fake record_latest view function."""
        return "<record latest>"

    @blueprint.route("/<any(doi):pid_scheme>/<path:pid_value>")
    def record_from_pid(*_: tuple, **__: dict) -> str:
        """Fake record_from_pid view function."""
        return "<record from pid>"

    return blueprint
