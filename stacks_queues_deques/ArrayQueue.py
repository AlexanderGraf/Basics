#!/usr/bin/python

# From Data Structures and Algorithms in Python - Goodrich et al.
# Chapter 6 - Stacks, Queues and Deques

class ArrayQueue():
    """FIFO queue using a Python list in a circular fashion as underlying storage"""
    DEFAULT_CAPACITY = 10 # assumed larger than any queue size needed

    def __init__(self):
        """Queue constructor"""
        self._data = None*ArrayQueue.DEFAULT_CAPACITY
        self._size = 0
        self._front = 0

    def __len__(self):
    	"""Return the number of elements in the queue"""
    	return self._size

    def is_empty(self):
    	"""Return True if the queue is empty"""
    	return self._size == 0

    def first(self):
    	"""Return (but don't remove) the element at the fron tof the queue"""
    	if self.is_empty():
    		raise Empty('queue is empty')
    	return self._data[self._front]

    def dequeue(self):
    	"""Remove and return the first element of the queue"""
    	if self.is_empty():
    		raise Empty('queue is empty')
    	# extract element of interest    	
        answer = self._data[self._front] 
        # aid garbage collection
        self._data[self._front] = None 
        # re-assign front taking care of circularity
        self._front = (self._front+1)%len(self._data) 
        # decrement the size
        self._size -= 1 
        return answer

    def enqueue(self,elem):
    	"""Append an element to the back of the queue"""
        if self._size == len(self._data):
        	self._resize(2*len(self._data))
        # find the end
        avail = (self._front+self._size)%len(self._data)
        self._data[avail] = elem
        self._size+=1

    def _resize(self,cap):
    	"""Double the capacity of the array/queue"""
        old = self._data
        self._data = [None]*cap
        walk = self._front
        # insert the old into the new
        for k in range(self._size):
        	self._data[k] = old[walk]
        	walk = (1+walk)%len(old)
        seld._front = 0





