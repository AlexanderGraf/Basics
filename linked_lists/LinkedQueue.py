#!/usr/bin/python

# From Data Structures and Algorithms in Python - Goodrich et al.
# Chapter 7 - Linked Lists

class LinkedQueue():
	"""FIFO Queue using a singly linked list for storage"""
	class _Node():
	    """Linked List node - nested subclass"""
	    __slots__ = "_element","_next" # streamline memory usage
        def __init__(self,element,nxt):
        	self._element = element
        	self._next = nxt

    # queue methods------------------    	
    def __init__(self):
        self._head = None
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
        return self._head._element

    def dequeue(self):
        """Remove and return the first element of the queue"""
        if self.is_empty():
            raise Empty("queue is empty")
        answer = self._head._element
        self._head = self._head._next
        self._size-=1
        if self.is_empty():
        	self._tail = None # the removed head had been the tail
        return answer

    def enqueue(self,elem):
        """Add an element to the back of the queue"""
        newest = self._Node(elem, None) # the new tail Node
        if self.is_empty():
        	self._head = newest # first element in queue
        else:
        	self._tail._next = newest
        self._tail = newest # update reference to the new tail
        self._size +=1
