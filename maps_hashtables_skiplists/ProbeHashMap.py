#!/usr/bin/python

# From Data Structures and Algorithms in Python - Goodrich et al.
# Chapter 10 -Maps, Hash Tables and Skip Lists

import HashMapBase

class ProbeHashMap(HashMapBase):
    """Hash map implemented with linear probing for collision resolution"""
    _AVAIL = object() # sentinel that marks locations of previous deletions

    def _is_available(self,j):
        """Return True if index j is available in table"""
        return self._table[j] is None or self._table[j] is ProbeHashMap._AVAIL

    def _find_slot(self,j,k):
        """Search for key k in bucket at index j
            Return (success, index) tuple, described as follows:
            if match was found, success is True and index denotes its location
            if no match found, success is False and index denotes first available slot
        """
        firstAvail=None
        while True:
            if self._is_available(j):
                if firstAvail is None:
                    firstAvail = j          # marked as first available slot
                if self._table[j] is None:
                    return (True, j)        # search has failed
            elif k == self._table[j]._key:
                return (True, j)            # found a match
            j = (j+1)%len(self._table)      # keep looking

    def _bucket_getitem(self,j,k):
        found, s = self._find_slot(j,k)
        if not found:
            raise KeyError("Key Error: "+repr(k))   # no match
        return self._table[s]._value


    def _bucket_setitem(self,j,k,v):
        found,s=self._find_slot(j,k)
        if not found:
            self._table[s]=self._Item(k,v)      # insert new item
            self._n+=1
        else:
            self._table[s]._value=v             # overwrite existing

    def _bucket_delitem(self,j,k):
        found, s = self._find_slot(j,k)
        if not found:
            raise KeyError("Key Error: "+repr(k))   # no match     
        self._table[s] = ProbeHashMap._AVAIL        # mark as vacated

    def __iter__(self):
        for j in range(len(self._table)):
            if not self._is_available(j):
                yield self._table[j]._key