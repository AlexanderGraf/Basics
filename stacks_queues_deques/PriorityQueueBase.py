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


class UnsortedPriorityQueue(PriorityQueueBase):
    """A min-oriented priority queue implemented with an unsorted list (requires Positional List)"""
    def _find_min(self):
        """Return position of item having the minimum key"""
        if self.is_empty():
            raise Empty('Priority queue is empty')
        small = self._data.first()
        walk = self._data.after()
        while walk is not in None:
            if walk.element()<small.element():
                small = walk
            walk = self._data.after(walk)
        return small

    def __init__(self):
        """Create a new and empty Priority Queue"""
        self._data = PositionalList()
    
    def __len__(self):
        """Return the number of items in the priority queue"""
        return len(self._data)

    def add(self,key,value):
        """Add a key-value pair"""
        self._data.add_last(self._Item(key,value)) # defined in PositionalList

    def min(self):
        """Return but do not remove (k,v) tuple with the minimum key"""
        p = self._find_min()
        item = p.element()
        return (item._key,item._value)

    def remove_min(self):
        """Remove and return tuple with the minimum key"""
        p = self._find_min()
        item = self._data.delete(p) # return the tuple deleted!
        return (item._key,item._value)


class SortedPriorityQueue(PriorityQueueBase):
    """A min-oriented priority queue implemented with a sorted list."""

    def __init__(self):
        """Create a new empty Priority Queue."""
        self._data = PositionalList()

    def __len__(self):
        """Return the number of items in the priority queue."""
        return len(self._data)

    def add(self, key, value):
        """Add a key-value pair."""
        # make new item instance
        newest = self._Item(key, value)
        # walk backward looking for smaller key
        walk = self._data.last()

        while walk is not None and newest < walk.element():
            walk = self._data.before(walk)
            if walk is None:
                # new key is smallest
                self._data.add_first(newest)
            else:
                # newest goes after walk
                self._data.add_after(walk, newest)

    def min(self):
        """Return but do not remove (k,v) tuple with minimum key."""
        if self.is_empty():
            raise Empty('Priority queue is empty.')

        p = self._data.first()
        item = p.element()
        return (item._key, item._value)

    def remove_min(self):
        """Remove and return (k,v) tuple with minimum key."""
        if self.is_empty():
            raise Empty('Priority queue is empty.')
        item = self. data.delete(self. data.first( ))
        return (item._key, item._value)