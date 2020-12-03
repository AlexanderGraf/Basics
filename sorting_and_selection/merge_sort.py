#!/usr/bin/python

# From Data Structures and Algorithms in Python - Goodrich et al.
# Chapter 12 - Sorting and Selection

def merge(S1,S2,S):
    """Merge two sorted Python lists S1 and S2 inthe properly sized list S"""
    i=j=0
    while i+j < len(S):
        if j == len(S2) or (i<len(S1) and S1[i]<S2[j]):
            S[i+j]=S1[i]            # copy the ith element of S1 as the next element in S
            i+=1
        else:
            S[i+j]=S2[j]            # copy the jth element of S2 as the next element of S
            j+=1
    return S


def merge_sort(S):
    """Sort the elements of a Python list S using a recursive merge-sort algorithm"""
    n = len(S)
    if n<2:
        return S                    # the list is already sorted
    
    # divide
    mid=n//2
    S1=S[0:mid]                     # copy of first half
    S2=S[mid:n]                     # copy of second half

    # conquer (using recursion)
    merge_sort(S1)                  # sort S1
    merge_sort(S2)                  # sort S2

    # merge results
    S = merge(S1,S2,S)              # merge sorted halves back into S
    return S