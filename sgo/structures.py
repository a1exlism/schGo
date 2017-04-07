# -*- coding: utf-8 -*-

"""
sgo.structures
==============

Data Structures
"""


class LookupDict(dict):
    """Dictionary lookup object."""

    def __init__(self, name=None):
        self.name = name
        super(LookupDict, self).__init__()

    def __repr__(self):
        return '<lookup \'%s\'>' % self.name

    def __getitem__(self, item):
        # allow fall-through here, so values default to None

        return self.__dict__.get(item, None)

    def get(self, key, default=None):
        return self.__dict__.get(key, default)
