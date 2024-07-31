#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jul 25 13:45:48 2024

@author: cameronmeharry
"""

from setuptools import setup, find_packages

setup(
    name='cpykg',
    version='0.0.1',
    packs =find_packages(),
    include_pack_data = True,
    package_data={
        'pyk_pack': ['data/*'],
    },
    # other setup parameters...
)