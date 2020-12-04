# From Data Structures and Algorithms in Python - Goodrich et al.
# Chapter 12 - Sorting and Selection

import random

def quick_select(S,k):
    """Return the kth smallest element of list S, for k from 1 to len(S)"""
    if len(S)==1:
        return S[0]
    pivot = random.choice(S)
