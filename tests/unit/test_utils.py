import pytest

from subway.utils import PartialDictComparer, AttributeDict


class A:
    def __init__(self):
        self.i = 0
        self.j = 1
        self.k = 2


class B(AttributeDict):
    pass


def test_partial_comparer():
    d = {
        'i': 0,
        'j': 1,
        'k': 2
    }

    assert PartialDictComparer(A()) == d

    del d['i']

    assert PartialDictComparer(A()) == d

    d['i'] = 666
    d['j'] = 3

    assert PartialDictComparer(A()) == d

    d['k'] = 5

    assert PartialDictComparer(A()) != d

    assert PartialDictComparer(A()) != {}

    d = {
        'x': 0,
        'y': 1,
        'z': 2
    }

    assert PartialDictComparer(A()) != d


def test_attributes_dict():
    b = B()
    b.i = 0
    b.j = 2
    b.k = 3

    assert b.i == 0
    assert b.j == 2
    assert b.k != 4

    assert b['i'] == 0
    assert b['j'] == 2
    assert b['k'] != 4

    for key in b.keys():
        if key == 'i':
            assert b[key] == 0
        elif key == 'j':
            assert b[key] == 2
        elif key == 'k':
            assert b[key] != 4
        else:
            assert b[key]
