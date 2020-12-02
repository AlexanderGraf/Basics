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


    # positional-based utility methods ---------------------
    def _set_red(self,p): p._node._red = True
    def _set_black(self,p): p._node._red = False
    def _set_color(self,p,make_red): p._node._red = make_red
    def _is_red(self,p): return p is not None and p._node._red
    def _is_red_leaf(self,p): return self._is_red(p) and self.is_leaf(p)

    def _get_red_child(self,p):
        """Return a red child of p (or None if no such child)"""
        for child in (self.left(p),self.right(p)):
            if self._is_red(child):
                return child
        return None

    # supprt for insertions ---------------------------------