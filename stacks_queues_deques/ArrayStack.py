#!/usr/bin/python

# From Data Structures and Algorithms in Python - Goodrich et al.
# Chapter 6 - Stacks, Queues and Deques

class Empty(Exception):
    """Error attempting to access an element from an empty container"""
    pass

class ArrayStack():
    """LIFO Stack using a Python list as underlying storage"""
    def __init__(self):
    	"""Stack constructor"""
    	self._data = []

    def __len__(self):
    	"""Return the number of elements in the stack"""
    	return len(self._data)

    def is_empty(self):
    	"""Return True if the stack is empty"""
    	return len(self._data) == 0

    def push(self,elem):
    	"""Add element to the top of the stack"""
    	self._data.append(elem)

    def top(self):
    	"""Return (but do not remove) the top element from the stack"""
        if self.is_empty():
        	raise Empty("stack is empty")
        return self._data[-1]

    def pop(self):
    	"""Remove and return the element from the top of the stack"""
    	if self.is_empty():
    		raise Empty("stack is empty")
        return self._data.pop()




