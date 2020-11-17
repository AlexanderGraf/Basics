#!/usr/bin/python

# From Data Structures and Algorithms in Python - Goodrich et al.
# Chapter 10 -Maps, Hash Tables and Skip Lists

import MapBase

class UnsortedTableMap(MapBase):
	"""Map implementation using an unordered list"""
	def __init__(self):
		"""Create an empty map."""
		# list of _Items
		self._table = []

	def __getitem__(self,k):
		"""Return value associated with key k - rais KeyError if not found"""
		for item in self._table:
			if k == item._key:
				return item._value
		raise KeyError('Key Error: '+repr(k))


    def __setitem__(self,k,v):
    	"""Assign value v to key k, overwriting the existing value if present"""
    	for item in self._table:
    		if k == item._key:
    			item._value = v
    			return
    	# did not find a match for key k
    	self._table.append(self._Item(k,v))

    def __delitem__(self,k):
    	for j in range(len(self._table)):
    		if k == self._table[j]._key: # find a match
    			self._table.pop(j)       # remove the item
    			return
        # item not found
		raise KeyError('Key Error: '+repr(k))

    def __len__(self):
        """Return the number of items in the map"""
        return len(self._table)

    def __iter__(self):
        """Generate an iteration of the map's keys"""
        for item in self._table:
            yield item._key
            