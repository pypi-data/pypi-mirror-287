#!/usr/bin/env python
# -*- coding: utf-8 -*-
# File: _version.py
#
# Copyright 2023 Marwin Baumann, Costas Tyfoxylos
#
# Licensed under the Apache License, Version 2.0 (the "License");
#  you may not use this file except in compliance with the License.
#  You may obtain a copy of the License at
#
# http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
#  distributed under the License is distributed on an "AS IS" BASIS,
#  WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#  See the License for the specific language governing permissions and
#  limitations under the License.
#

"""
Manages the version of the package.

.. _Google Python Style Guide:
   https://google.github.io/styleguide/pyguide.html

"""

import os

__author__ = '''Marwin Baumann <mbaumann@schubergphilis.com>, Costas Tyfoxylos <ctyfoxylos@schubergphilis.com>'''
__docformat__ = '''google'''
__date__ = '''21-11-2023'''
__copyright__ = '''Copyright 2023, Marwin Baumann, Costas Tyfoxylos'''
__credits__ = ["Ben van Breukelen", "Costas Tyfoxylos", "Marwin Baumann"]
__license__ = '''Apache Software License 2.0'''
__maintainer__ = '''Ben van Breukelen, Costas Tyfoxylos, Marwin Baumann'''
__email__ = '''<bvanbreukelen@schubergphilis.com>,<ctyfoxylos@schubergphilis.com>,<mbaumann@schubergphilis.com>'''
__status__ = '''Development'''  # "Prototype", "Development", "Production".

VERSION_FILE_PATH = os.path.abspath(
    os.path.join(
        os.path.dirname(__file__),
        '..',
        '.VERSION'
    )
)

LOCAL_VERSION_FILE_PATH = os.path.abspath(
    os.path.join(
        os.path.dirname(__file__),
        '.VERSION'
    )
)

try:
    with open(VERSION_FILE_PATH, encoding='utf8') as f:
        __version__ = f.read()
except IOError:
    try:
        with open(LOCAL_VERSION_FILE_PATH, encoding='utf8') as f:
            __version__ = f.read()
    except IOError:
        __version__ = 'unknown'
