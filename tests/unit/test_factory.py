# MIT License

# Copyright (c) 2016 Alexis Bekhdadi (midoriiro) <contact@smartsoftwa.re>

# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:

import pytest

from subways.factory import Factory


class A:
    def __init__(self, i, j, k, l):
        self.i = i
        self.j = j
        self.k = k
        self.l = l
        self.d = [
            1,
            2,
            3
        ]


@pytest.fixture
def template():
    return Factory.create(A, i=0, j=1, k=2, l=3)


def test_create(template):
    assert template.i == 0 and \
        template.j == 1 and \
        template.k == 2 and \
        template.l == 3


def test_clone(template):
    obj = Factory.clone(template)

    template.i = 5
    template.d = [4, 5, 6]

    assert obj.i == 5 and \
        obj.j == 1 and \
        obj.k == 2 and \
        obj.l == 3 and \
        obj.d == [4, 5, 6]


def test_copy(template):
    b = A(i=666, j=777, k=888, l=999)

    template.d = b

    obj = Factory.copy(template)

    template.i = 5
    obj.i = 2

    assert obj.i != template.i and \
        obj.j == template.j and \
        obj.k == template.k and \
        obj.l == template.l and \
        obj.d == template.d


def test_deepcopy(template):
    b = A(i=666, j=777, k=888, l=999)

    template.d = b

    obj = Factory.deepcopy(template)

    template.i = 5
    obj.i = 2

    assert obj.i != template.i and \
        obj.j == template.j and \
        obj.k == template.k and \
        obj.l == template.l and \
        obj.d != template.d
