# TODO: write module, function, class, method docstring
# pylint: disable=missing-docstring

import os
import pytest


def get_data_path(filename):
    base = os.path.join(
        os.path.dirname(os.path.realpath(__file__)), 'data'
    )

    return os.path.join(base, filename)
