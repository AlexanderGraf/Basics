#!/usr/bin/python

# From Data Structures and Algorithms in Python - Goodrich et al.
# Chapter 11 - Search Trees

import TreeMap

class RedBlackTreeMap(TreeMap):
	"""Sorted map implementation using a red black tree."""
    class _Node(TreeMap._Node):
        """Node class for red black tree maintains bit that denotes color."""
        __slots__ = '_red'      # additional data member to the Node class

        def __init__(self,element,parent=None,left=None,right=None):
            super().__init__(element,parent,left,right)
            self._red = True    # new node red by default

            