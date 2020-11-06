#!/usr/bin/python

# From Data Structures and Algorithms in Python - Goodrich et al.
# Chapter 9 - Priority Queues

class PriorityQueueBase():
    """Abstract base class for a priority queue"""
    class _Item():
        __slots__ = '_key', '_value'

        def __init__(self, k,v):
            self._key = k
            self._value = v

        def __lt__(self,other):
            """Compare items based on their keys"""
            return self._key<other._key

    def is_empty(self):
        """Return True if the priority queue is empty"""
        return len(self) == 0


class HeapPriorityQueue(PriorityQueueBase):
    """A min-oriented priority queue implemented with a binary heap in an array"""
    
    # non public ------------- 
    def _parent(self,j):
        return (j-1)//2

    def _left(self,j):
        return 2*j+1

    def _right(self,j):
        return 2*j+2

    def _has_left(self,j):
        return self._left(j) < len(self._data)

    def _has_right(self,j):
        return self._right(j) < len(self._data)

    def _swap(self,i,j):
        """Swap the elements at indices i and j of the array"""
        self._data[i], self._data[j] = self._data[i]

    def _upheap(self,j):
        parent = self._parent(j)
        if j>0 and self._data[j] < self._data[parent]
            self._swap(j,parent)
            self._upheap(parent)
    
    def _downheap(self,j):
        if self._has_left(j)
            left = self._left()
            small_child = left
            if self._has_right(j):
                right = self._right(j)
                if self._data[right] < self._data[left]:
                    small_child = right
                if self._data[small_child]<self._data[j]:
                    self._swap(j,small_child)
                    self._downheap(small_child) # recur at position of small_child

    # public ------------------
    def __init__(self, contents=()):
        """Create a new empty Priority Queue
        By default queue will be empty. If contents argument is given, it should 
        be as an iterable sequence of (k,v) tuples specifying the initial contents.
        """
        self._data = [self._Item(k,v) for k,v in contents]
        if len(self._data)>1:
            self._heapify()

    def _heapify(self):
        start = self._parent(len(self)-1) # the parent of the last leaf
        for j in range(start,-1,-1): # walk backwards to the root inclusive
            self._downheap(j)

    def __len__(self):
        """Return the number of items in the priority queue"""
        return len(self._data)

    def add(self,key,value):
        """Add a key value pair to the priority queue"""
        self._data.append(self._Item(key,value))
        self._upheap(len(self._data)-1) # upheap newly added position

    def min(self):
        """Return but do not remove (k,v) tuple with minimum key"""
        if self.is_empty():
            raise Empty('Priority queue is empty')

        item = self._data[0] # the root by definition
        return (item._key, item._value)

    def remove_min(self):
        """Remove and return (k,v) tuple with minimum key"""
        if self.is_empty():
            raise Empty('Priority queue is empty')
        # put min (the root) at the end
        self._swap(0,len(self._data)-1)
        # remove it (item is it, but outside of the ADT)
        item = self._data.pop()
        self._downheap(0)
        return(item._key,item._value)
