#!/usr/bin/env bash
# -*- coding: utf-8 -*-
#
# Copyright (C) 2021 Graz University of Technology.
#
# repository-cli is free software; you can redistribute it and/or modify it
# under the terms of the MIT License; see LICENSE file for more details.


python -m check_manifest --ignore ".*-requirements.txt" && \
python -m sphinx.cmd.build -qnNW docs docs/_build/html && \
python -m pytest
