# -*- coding: utf-8 -*-
#
# Copyright (C) 2021-2023 Graz University of Technology.
#
# repository-cli is free software; you can redistribute it and/or modify it
# under the terms of the MIT License; see LICENSE file for more details.

"""Commonly used options for CLI commands."""


import click


def option_quiet():
    """Get parameter option for quiet."""
    return click.option(
        "--quiet",
        is_flag=True,
        default=False,
        type=click.BOOL,
    )


def option_jq_filter():
    """Get parameter option for jq filter."""
    return click.option(
        "--jq-filter",
        default=".",
        type=click.STRING,
        required=False,
        help="filter for jq",
    )


def option_data_model():
    """Get parameter option for data model."""
    return click.option(
        "--data-model",
        type=click.Choice(["rdm", "marc21"]),
        default="rdm",
    )


def option_record_type():
    """Get parameter option for record type."""
    return click.option(
        "--record-type",
        type=click.Choice(["record", "draft"], case_sensitive=True),
        default="record",
    )


def option_identifier(required: bool = True):
    """Get parameter options for metadata identifier.

    Sample use: --identifier '{ "identifier": "10.48436/fcze8-4vx33", "scheme": "doi"}'
    """
    return click.option(
        "--identifier",
        "-i",
        required=required,
        help="metadata identifier as JSON",
    )


def option_pid_identifier(required: bool = True):
    """Get parameter options for metadata identifier.

    Sample use: --pid-identifier '{"doi": {"identifier": "10.48436/fcze8-4vx33", "provider": "unmanaged"}}'
    """
    return click.option(
        "--pid-identifier",
        "--pid-identifier",
        "pid_identifier",
        required=required,
        help="pid identifier as JSON",
    )


def option_pid(required: bool = True):
    """Get parameter options for record PID.

    Sample use: --pid "fcze8-4vx33"
    """
    return click.option(
        "--pid",
        "-p",
        metavar="PID_VALUE",
        required=required,
        help="persistent identifier of the object to operate on",
    )


def option_input_file(required: bool = True, type_=click.File("r")):
    """Get parameter options for input file.

    Sample use: --input-file "input.json"
    """
    return click.option(
        "--input-file",
        "--if",
        "input_file",
        metavar="string",
        required=required,
        help="name of file to read from",
        type=type_,
    )


def option_output_file(required: bool = True):
    """Get parameter options for output file.

    Sample use: --output-file "output.json"
    """
    return click.option(
        "--output-file",
        "--of",
        "output_file",
        metavar="string",
        required=required,
        help="name of file to write to",
        type=click.File("w"),
    )