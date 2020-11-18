#!/usr/bin/python

# From Data Structures and Algorithms in Python - Goodrich et al.
# Chapter 11 - Search Trees

import LinkedBinaryTree, MapBase

class TreeMap(LinkedBinaryTree, MapBase):
    """Sorted map implementation using a binary serach tree"""

    # override Position class ------------
    class Position(LinkedBinrayTree.Position):
        def key(self):
            """Return key of map's key value pair"""
            return self.element()._key    

        def value(self):
            """Return value of map's key value pair"""
            return self.element()._value   

    # nonpublic --------------------------
    def _subtree_search(self,p,k):
        """Return Position of p's subtree having key, k or last node searched"""
        if k == p.key():            # found match
            return p
        elif k < p.key():           # search left subtree
            if self.left(p) is not None:
                return self._subtree_search(self.left(p),k)
        else:                       # search right subtree
            if self.right(p) is not None:
                return self._subtree_search(self.right(p),k)
        return p

    def _subtree_first_position(self,p):
        """Return Position of first item in subtree rooted at p"""
        walk = p                    
        while self.left(walk) is not None: # keep walking left
            walk = self.left(walk)
        return walk

    def _subtree_last_position(self,p):
        """Return Position of last item in subtree rooted at p"""
        walk = p                    
        while self.right(walk) is not None: # keep walking right
            walk = self.right(walk)
        return walk

