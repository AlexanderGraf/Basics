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

    # public ------------------------------
    def first(self):
        """Return the first position in the tree (or None if empty)"""
        return self._subtree_first_position(self.root()) if len(self)>0 else None

    def last(self):
        """Return the last Position in the tree (of None if empty)"""
        return self._subtree_last_position(self.root()) if len(self)>0 else None

    def before(self,p):
        """Return the position just before p in the natural order
        Return None if p is the first position
        """
        self._validate(p)   # inherited from LinkedBinaryTree
        if self.left(p):
            return self._subtree_last_position(self.left(p))
        else:
            # walk upward
            walk = p
            above = self.parent(walk)
            while above is not None and walk == self.left(above):
                walk = above
                above = self.parent(walk)
            return above

    def after(self,p):
        """Return the position just after p in the natural order
        Return None if p is the last position
        """
        self._validate(p)   # inherited from LinkedBinaryTree
        if self.right(p):
            return self._subtree_first_position(self.right(p))
        else:
            # walk downward
            walk = p
            below = self.parent(walk)
            while below is not None and walk == self.right(below):
                walk = below
                below = self.parent(walk)
            return below

    def find_position(self,k):
        """Return position with key k, or else neighbor (or NOne if empty)"""
        if self.is_empty():
            return None
        else:
            p = self._subtree_search(self.root(),k)
            self._rebalance_access(p) # hook for balanced tree subclass
            return p

    def