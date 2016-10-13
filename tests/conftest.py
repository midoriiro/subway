# MIT License

# Copyright (c) 2016 Alexis Bekhdadi (midoriiro) <contact@smartsoftwa.re>

# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:

# TODO: write module, function, class, method docstring
# pylint: disable=missing-docstring

import os
import pytest


def get_data_path(filename):
    base = os.path.join(
        os.path.dirname(os.path.realpath(__file__)), 'data'
    )

    return os.path.join(base, filename)
