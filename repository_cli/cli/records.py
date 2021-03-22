# -*- coding: utf-8 -*-
#
# Copyright (C) 2021 Graz University of Technology.
#
# repository-cli is free software; you can redistribute it and/or modify it
# under the terms of the MIT License; see LICENSE file for more details.

"""Management commands for records."""

import json

import click
from flask.cli import with_appcontext
from flask_principal import Identity
from invenio_rdm_records.proxies import current_rdm_records

from .click_options import option_identifier, option_pid
from .util import get_identity


@click.group()
def records():
    """Management commands for records."""
    pass


@click.group()
def identifiers():
    """Management commands for record identifiers."""
    pass


records.add_command(identifiers)


# invenio repository records identifiers list
@identifiers.command("list")
@option_pid
@with_appcontext
def list_identifiers(pid):
    """List record's identifiers."""
    identity = get_identity()
    service = current_rdm_records.records_service
    record_data = service.read(id_=pid, identity=identity).data.copy()
    current_identifiers = record_data["metadata"].get("identifiers", [])

    if len(current_identifiers) == 0:
        fg = "yellow"
        click.secho("record does not have any identifiers", fg=fg)

    for index, identifier in enumerate(current_identifiers):
        # BLACK, RED, GREEN, YELLOW, BLUE, MAGENTA, CYAN, WHITE, RESET
        fg = "blue" if index % 2 == 0 else "cyan"
        click.secho(json.dumps(identifier, indent=2), fg=fg)


# invenio repository records identifiers add -p "fcze8-4vx33" -i '{ "identifier": "10.48436/fcze8-4vx33", "scheme": "doi"}'
@identifiers.command("add")
@option_identifier
@option_pid
@with_appcontext
def add_identifier(identifier, pid):
    """Update the specified record's identifiers."""
    identifier = json.loads(identifier)
    if type(identifier) is not dict:
        click.secho(f"identifier should be of type dictionary", fg="red")
        return

    identity = get_identity("system_process")
    service = current_rdm_records.records_service

    # get current draft or create new one
    record_data = service.edit(id_=pid, identity=identity).data.copy()
    current_identifiers = record_data["metadata"].get("identifiers", [])
    current_schemes = [_["scheme"] for _ in current_identifiers]
    scheme = identifier["scheme"]
    if scheme in current_schemes:
        click.secho(f"scheme '{scheme}' already in identifiers", fg="red")
        return

    current_identifiers.append(identifier)
    record_data["metadata"]["identifiers"] = current_identifiers

    try:
        service.update_draft(id_=pid, identity=identity, data=record_data)
        service.publish(id_=pid, identity=identity)
        click.secho(pid, fg="green")
    except Exception as e:
        service.delete_draft(id_=pid, identity=identity)
        click.secho(f"{pid}, {e}", fg="red")

    return


# invenio repository records identifiers replace -p "fcze8-4vx33" -i '{ "identifier": "10.48436/fcze8-4vx33", "scheme": "doi"}'
@identifiers.command("replace")
@option_identifier
@option_pid
@with_appcontext
def replace_identifier(identifier, pid):
    """Update the specified record's identifiers."""
    identifier = json.loads(identifier)
    if type(identifier) is not dict:
        click.secho(f"identifier should be of type dictionary", fg="red")
        return

    identity = get_identity("system_process")
    service = current_rdm_records.records_service

    # get current draft or create new one
    record_data = service.edit(id_=pid, identity=identity).data.copy()
    current_identifiers = record_data["metadata"].get("identifiers", [])
    scheme = identifier["scheme"]
    replaced = False
    for index, ci in enumerate(current_identifiers):
        if ci["scheme"] == scheme:
            current_identifiers[index] = identifier
            replaced = True
            break

    if not replaced:
        click.secho(f"scheme '{scheme}' not in identifiers", fg="red")
        return

    record_data["metadata"]["identifiers"] = current_identifiers

    try:
        service.update_draft(id_=pid, identity=identity, data=record_data)
        service.publish(id_=pid, identity=identity)
        click.secho(pid, fg="green")
    except Exception as e:
        service.delete_draft(id_=pid, identity=identity)
        click.secho(f"{pid}, {e}", fg="red")

    return
