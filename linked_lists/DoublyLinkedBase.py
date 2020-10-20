#!/usr/bin/python

# From Data Structures and Algorithms in Python - Goodrich et al.
# Chapter 7 - Linked Lists

class DoublyLinkedBase():

	class _Node():
		"""Lightweight non-public class for storing a doubly linked node"""
		__slots__ = "_element","_prev","_next" # streamline memory
		def __init__(self,element,prev,next):
            self._element = element
            self._prev = prev
            self._next = next

    def __init__(self):
        """Create an empty list"""
        self._header = self._Node(None,None,None)
        self._trailer = self._Node(None,None,None)
        self._header._next = self._trailer
        self._trailer._prev = self._header
        self._size = 0

    def __len__(self):
    	"""Return the number of elements in the list"""
    	return self._size

    def is_empty(self):
    	"""Return True if list if empty"""
    	return self._size == 0

    def _insert_between(self,elem,predecessor,successor):
    	"""Add element between two existing nodes and return new node"""
    	newest = self._Node(elem,predecessor,successor)
    	predecessor._next = newest
    	successor._prev = newest
    	self._size += 1
    	return newest

    def _delete_node(self,node):
    	"""Delete nonsentinel node from the list and return its element"""
    	predecessor = node._prev
    	successor = node._next
        predecessor._next = successor
        successor._prev = predecessor
        self._size-=1
        element = node._element # record element before deletion
        node._prev = node._next = node._element = None # deprecate node
        return element



