#!/usr/bin/python

# From Data Structures and Algorithms in Python - Goodrich et al.
# Chapter 7 - Linked Lists

class PositionalList(_DoublyLinkedBase):
    """A sequential container of elements allowing positional access"""

    class Position():
        """An abstraction representing the positional location of an element"""
        def __init__(self,container,node):
            self._container = container
            self._node = node

        def element(self):
            """Return the element stored at this position"""
            return self._node._element

        def __eq__(self,other):
            """Return True if other is a Position representing the same location"""
            return type(other) is type(self) and other._node is self._node

        def __ne__(self,other):
        	"""Return True if other is does not represent the same location"""
            return not (self == other)

    # utilities --------------
    def _validate(self,p):
        """Return position's node or raise appropriate erro if invalid"""
        if not isinstance(p, self.Position):
            raise TypeError("p must be a proper Position type")
        if p._container is not self:
            raise ValueError("p does not belong to this container")
        if p._node._next is None:
            raise ValueError("p is no longer valid")
        return p._node
    
    def _make_position(self,node):
        """Return position instance for the given node (or None if a sentinel)"""
        if node is self._header or node is self._trailer:
            return None
        else:
            return self.Position(self,node)

    # accessor methods -------
    def first(self):
        """Return the first position in the list (or None if empty)"""
        return self._make_position(self._header._next)

    def last(self):
        """Return the last position in the list (or None if empty)"""
        return self._make_position(self._trailer._prev)	

    def before(self,p):
        """Return the Position just before Position p (or None if p is first)"""
        node = self._validate(p)
        return self._make_position(node._prev)

    def after(self,p):
        """Return the Position just after Position p (or None if p is last)"""
        node = self._validate(p)
        return self._make_position(node._next)        

    def __iter__(self):
        """Generate a forward iteration of the elements of the list"""
        cursor = self.first()
        while cursor is not None:
            yield cursor.element()
            cursor = self.after(cursor)

    # mutators ---------------
    # override inheritied version to return Position rather than Node
    def _insert_between(self,e,predecessor,successor):
        """Add element between existing nodes and return new Position"""
        node = super()._insert_between(e,predecessor,successor)
        return self._make_position(node)

    def add_first(self,e):
        """Insert element e at the front of the list and return new Position"""
        return self._insert_between(e, self._header,self._header._next)

    def add_last(self,e):
        """Insert element e at the back of the list and return the new Position"""
        return self._insert_between(e,self._trailer._prev,self._trailer)

    def add_before(self,p,e):
        """Insert element e into list before Position p and return new Position."""
        original = self._validate(p)
        return self._insert_between(e, original._prev, original)

    def add_after(self,p,e):
        """Insert element e into list after Position p and return new Position."""
        original = self._validate(p)
        return self._insert_between(e, original, original._next)

    def delete(self,p):
        """Remove and return the element at Position p"""
        original = self._validate(p)
        return self._delete_node(original)

    def replace(self,p):
    	"""Replace the element at Position p with e
    	Return the element formerly at Position p
    	"""
    	original = self._validate(p)
    	old_value = original._element
    	original._element = e
    	return old_value


