# MIT License

# Copyright (c) 2016 Alexis Bekhdadi (midoriiro) <contact@smartsoftwa.re>

# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:

'''
    Factory is a module to create, clone, copy or deepcopy a object.
'''

import copy


class Factory:
    '''
        Factoryze object.
    '''

    @staticmethod
    def create(template, **kwargs):
        '''
            Create an instance object.

            :param template: The class non instancied
            :param **kwargs: A dictionary of attributes class
            :return: Return a created instance object
        '''

        return template(**kwargs)

    @staticmethod
    def clone(obj):
        '''
            Clone an instance object.

            :param: obj: An instance of object
            :return: Return a cloned object
        '''
        clone = obj
        return clone

    @staticmethod
    def copy(obj):
        '''
            Copy an instance object.

            :param: obj: An instance of object
            :return: Return a copy of the object.
        '''
        return copy.copy(obj)

    @staticmethod
    def deepcopy(obj):
        '''
            Deep copy an instance object.

            :param: obj: An instance of object
            :return: Return a deep copy of the object
        '''
        return copy.deepcopy(obj)
