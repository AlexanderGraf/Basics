#!/usr/bin/python

# From Data Structures and Algorithms in Python - Goodrich et al.
# Chapter 8 -Trees

class EurlerTour():
    """Abstract base class for performing an Euler tour
    _hook_previsit and _hook_postvisit may be overridden by subclasses
    """
    def __init__(self,tree):
        """Prepare and Euler tour for a given tree"""
        self._tree = tree

    def tree(self):
        """Return reference to the tree being traversed"""
        if len(self._tree)>0:
            # start the recursion
            return self._tour(self._tree.root(),0,[])

    def _tour(self,p,d,path):
        """
        Perform tour of subtree rooted at Position p.
        p - Position of current node being visited
        d - depth of p in the tree
        path - list of indices of children on path from root to p
        """
        self._hook_previsit(p,d,path)
        results = []
        # add new index to end of path before recursion
        path.append(0)
        for c in self._tree.children(p):
            # recur on child's subtree
            results.append(self._tour(c,d+1,path))
            # increment index
            path[-1]+=1
        # remove extraneous index from end of path
        path.pop()
        answer = self._hook_postvisit(p, d, path, results)
        return answer

    def _hook_previsit(self, p, d, path):
        pass

    def _hook_postvisit(self, p, d, path):
        pass