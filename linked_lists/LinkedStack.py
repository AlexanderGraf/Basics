#!/usr/bin/python

# From Data Structures and Algorithms in Python - Goodrich et al.
# Chapter 7 - Linked Lists

class Empty(Exception):
    """Error attempting to access an element from an empty container"""
    pass

class LinkedStack():
    """LIFO Stack using a singly linked list for storage"""
    class _Node():
        """Linked List node - nested subclass"""
        __slots__ = "_element","_next" # streamline memory usage
        def __init__(self,element,nxt):
        	self._element = element
        	self._next = nxt

    # stack methods------------------
    def __init__(self):
        """Stack constructor"""
        self._head = None
        self._size = 0

    def __len__(self):
    	"""Return the number of elements in the stack"""
        return self._size

    def is_empty(self):
    	"""Return true if the stack is empty"""
        return self._size == 0

    def push(self,elem):
        """Add element to the top of the stack"""
        self._head = self._Node(elem,self._head)
        self._size +=1

    def top(self):
        """Return (but do not remove) the element at the top of the stack"""
        if self.is_empty():
        	raise Empty("stack is empty")
        # top of the stack is at the head of the list
        return self._head._element

    def pop(self):
        """Remove and return the element from the top of the stack"""
        if self.is_empty():
        	raise Empty("stack is empty")
        answer = self._head._element
        self._head = self._head._next
        self._size-=1
        return answer