#!/usr/bin/python

# From Data Structures and Algorithms in Python - Goodrich et al.
# Chapter 7 - Linked Lists

class CircularQueue():
	"""Queue implementation using circular linked list"""
	class _Node():
		"""Linked List node - nested subclass"""
		__slots__ = "_element","_next" # streamline memory usage
        def __init__(self,element,nxt):
        	self._element = element
        	self._next = nxt

    # queue methods------------------   
    def __init__(self):
    	self._tail = None
    	self._size = 0		

    def __len__(self):
    	"""Return the number of elements in the queue"""
    	return self._size

    def is_empty(self):
    	"""Return true if the stack is empty"""
    	return self._size == 0

    def first(self):
        """Return (but do not remove) the front of the queue"""
    	if self.is_empty():
    		raise Empty("queue is empty")
    	head = self._tail._next
        return head._element

    def dequeue(self):
    	"""Remove and return the first element of the queue"""
    	if self.is_empty():
    		raise Empty("queue is empty")
    	oldhead = self._tail._next
    	if self._size == 1:
    	    self._tail = None
    	else:
    	    self._tail._next = oldhead._next
    	self._size -=1
    	return oldhead._element    	

    def enqueue(self,elem):
        """Add an element to the back of the queue"""
        newest = self._Node(elem,None)
    	if self.is_empty():
    		newest._next = newest
    	else:
    		newest._next = self._tail._next
    	self._tail = newest
    	self._size +=1 

    def rotate(self):
        """Rotate front element to the back of the queue"""
        if self._size > 0:
        	self._tail = self._tail._next # old head becomes new tail
        