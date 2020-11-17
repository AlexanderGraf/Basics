#!/usr/bin/python

# From Data Structures and Algorithms in Python - Goodrich et al.
# Chapter 10 -Maps, Hash Tables and Skip Lists

from collections.abc import MutableMapping

class MapBase(MutableMapping):
    """Our own abstract base class that includes a nonpublic _Item class"""
    class _Item():
        """Lightweight composite to store key-value pairs as map items"""
        __slots__ = '_key', '_value'

        def __init__(self,k,v):
            self._key = k
            self._value = v

        def __eq__(self,other):
            # compares items based on thier keys
            return self._key == other._key

        def __ne__(self,other):
            return not (self == other)

        def __lt__(self,other):
            # inequality check based on keys
            return self._key < other._key

        def __gt__(self,other):
            # inequality check based on keys
            return self._key > other._key