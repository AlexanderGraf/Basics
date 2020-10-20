#!/usr/bin/python

# From Data Structures and Algorithms in Python - Goodrich et al.
# Chapter 7 - Linked Lists

# requires importing DoublyLinkedBase class

class LinkedDeque(DoublyLinkedBase):
    """Double-ended queue implementation based on a doubly linked list"""
    def __init__(self):
        pass

    def first(self):
        """Return (but do not remove) the element at the front of the dequeue"""
        if self.is_empty():
            raise Empty("deque is empty")
        return self._header._next._element

    def insert_first(self,elem):
           """Add an element to the front of the deque"""
           self._insert_between(elem,self._trailor._prev, self._header._next) # after header

    def insert_last(self,elem):
       	"""Add an element to the back of the deque"""
       	self._insert_between(elem,self._trailor._prev, self._trailor) # before trailor

    def delete_first(self):
       	"""Remove and return the element from the front of the deque"""
        if self.is_empty():
            raise Empty("deque is empty")    
        return self._delete_node(self._header._next)	


    def delete_last(self):
        """Remove and return the element from the back of the deque"""
        if self.is_empty():
            raise Empty("deque is empty")    	
        return self._delete_node(self._trailor._prev)	