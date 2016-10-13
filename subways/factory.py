# TODO: write module, function, class, method docstring
# pylint: disable=missing-docstring

import copy


class Factory:
    @staticmethod
    def create(template, **kwargs):
        return template(**kwargs)

    @staticmethod
    def clone(obj):
        clone = obj
        return clone

    @staticmethod
    def copy(obj):
        return copy.copy(obj)

    @staticmethod
    def deepcopy(obj):
        return copy.deepcopy(obj)
