# TODO: write module, function, class, method docstring
# pylint: disable=missing-docstring


class AttributeDict(dict):
    def __getattr__(self, key):
        return self[key]

    def __setattr__(self, key, value):
        self[key] = value

    def __delattr__(self, key):
        del self[key]


class PartialDictComparer(dict):
    def __init__(self, obj):
        super().__init__()

        self._obj = obj

    def __ne__(self, other):
        return not self.__eq__(other)

    def __eq__(self, other):
        if not other:
            return False

        attrs = dir(self._obj)
        attrs = [key for key in other.keys() if key in attrs]

        if not attrs:
            return False

        for attr in attrs:
            if getattr(self._obj, attr) == other[attr]:
                return True

        return False
