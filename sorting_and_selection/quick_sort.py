# From Data Structures and Algorithms in Python - Goodrich et al.
# Chapter 12 - Sorting and Selection

import LinkedQueue

def quick_sort(S):
    """Sort the elements of queue S using a recursive quick-sort algorithm"""
    n=len(S)
    if n<2:
        return 				# already sorted
    
    # divide
    p=S.first()             # use first as an arbitrary pivot
    L=LinkedQueue()         # Lower
    E=LinkedQueue()         # Equal
    G=LinkedQueue()         # Greater
    while not S.is_empty(): # divide S into L, E and G
        if S.first()<p:
            L.enqueue(S.dequeue())
        elif p<S.first():
            G.enqueue(S.dequeue())
        else:
            E.enqueue(S.dequeue())  # S.first() must equal the pivot

    # conquer
    quick_sort(L)           # sort elements less than p
    quick_sort(G)           # sort elements greater than p

    # concatenate results
    while not L.is_empty():
        S.enqueue(L.dequeue())
    while not E.is_empty():
        S.enqueue(E.dequeue())
    while not G.is_empty():
        S.enqueue(G.dequeue())
