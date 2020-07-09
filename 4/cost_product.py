"""
Matrix multiplication in Cost-categories.
"""
from functools import reduce
import numpy as np
import pandas as pd
import networkx as nx

# TODO
# testing
class Obj:

    def __init__(self, obj):
        if isinstance(obj, Obj):
            self = obj
        if isinstance(obj, (list, set)):
            self._items = map(self.__init__, obj)
        if not isinstance(obj, collections.Hashable):
            raise TypeError('Objects need to be hashable')
        self._items = obj

class Arrow:

    def __init__(self, src, tgt, data=None):
        self.src = Obj(src)
        self.tgt = Obj(tgt)
        self.data = data # enrichment

class Category:

    def __init__(self, obj, arr):
        self.obj = obj
        self.arr = arr # arrows can have any type -> enrichment

    def _from_graph(self, g):
        self.obj = g.nodes
        self.arr = g.edges

    @property
    def obj(self):
        return self._obj

    @obj.setter
    def obj(self, new):
        # TODO
        self._obj = Obj(new)

    @property
    def arr(self):
        return self._arr

    @arr.setter
    def arr(self, new):
        # TODO
        self._arr = new

class Functor: # TODO
    pass
class Profunctor(Functor):

    def __init__(self, p, src=None, tgt=None):
        self._src = src or list(range(p.shape[0]))
        self._tgt = tgt or list(range(p.shape[1]))
        self.p = pd.DataFrame(self._wrap(p), index=self._src, columns=self._tgt)

    def __mul__(self, other):
        pass

    def _wrap(self, other):
        pass
class Quantale:

    def __init__(self, *args, **kwds):
        self._args = args
        self._kwds = kwds

    # Preorder
    def __eq__(self, other): raise NotImplementedError
    def __ne__(self, other): return not self.__eq__(other)
    def __le__(self, other): raise NotImplementedError
    def __lt__(self, other): return self.__le__(other) and not self.__eq__(other)
    def __ge__(self, other): return self._wrap(other).__le__(self)
    def __gt__(self, other): return self.__ge__(other) and not self.__eq__(other)
    
    # Multiplication
    def __mult__(self, other): raise NotImplementedError
    def hom(self, other): raise NotImplementedError
    @property
    def unit(self): raise NotImplementedError
    def __pow__(self, n : int): return reduce(lambda x,y: x*y, [self.x]*n)
    
    # Addition
    def __add__(self, other): self.join(other)
    @classmethod
    def join(cls, *args):
        return reduce(lambda x, y: x.join(y), map(cls, args))

    def join(self, other):
        raise NotImplementedError
    
    @property
    def zero(self): raise NotImplementedError

    # Printing
    def __repr__(self):
        return 'Quantale {} {}'.format(self._args, self._kwds)
    
    def __str__(self):
        return self.__repr__()
    
    # Helpers
    def _wrap(self, other):
        if isinstance(other, self.__class__):
            return other
        return self.__class__(other)

class Bool(Quantale):

    def __init__(self, x : bool):
        self._x = x

    # Preorder
    def __eq__(self, other): return self._x.__eq__(self._wrap(other)._x)
    def __le__(self, other): return self._x.__le__(self._wrap(other)._x)

    # Multiplication
    def __mult__(self, other): return self._wrap(self._x and self._wrap(other)._x)
    def hom(self, other): return self._wrap((not self._x) or self._wrap(other)._x)
    @property
    def unit(self): return self._wrap(True)

    # Addition
    def join(self, other): return self._wrap(self._x or self._wrap(other)._x)
    @property
    def zero(self): return self._wrap(False)

    # Printing
    def __repr__(self): return 'Bool {}'.format(self._x)

class Cost(Quantale):

    def __init__(self, x : np.float):
        self._x = x

    # Preorder
    def __eq__(self, other): return self._x.__eq__(self._wrap(other)._x)
    def __le__(self, other): return self._x.__le__(self._wrap(other)._x)

    # Multiplication
    def __mul__(self, other): return self._wrap(self._x + self._wrap(other)._x)
    def hom(self, other): return self._wrap(self._wrap(other)._x - self._x)
    @property
    def unit(self): return self._wrap(np.inf)

    # Addition
    def join(self, other): return self._wrap(min(self._x, self._wrap(other)._x))
    @property
    def zero(self): return self._wrap(0)

    # Printing
    def __repr__(self): return 'Cost {}'.format(self._x)

    
def one_step_distance_matrix(g):
    #n = g.number_of_nodes()
    v = list(g.nodes)
    e = pd.DataFrame([[0 if k==j else np.inf for k in g.nodes] for j in g.nodes], index=v, columns=v)
    d = e.copy()

    for edge in g.edges:
        a, b = edge
        d.loc[a,b] = g.edges[edge]['weight']

    return d
    
def distance_matrix(g):
    n = g.number_of_nodes()
    v = list(g.nodes)
    e = pd.DataFrame([[0 if k==j else np.inf for k in g.nodes] for j in g.nodes], index=v, columns=v)
    d = one_step_distance_matrix(g)
    d = pd.DataFrame(reduce(lambda x,y: cost_mult(x,y), [d]*n, e), index=v, columns=v)

    return d

def cost_mult(a, b):
    """

    Args:
        a ([type]): [description]
        b ([type]): [description]
    """

    c = pd.DataFrame(np.inf, index=a.index, columns=b.columns)

    for i, row in a.iterrows():
        for j, col in b.T.iterrows():
            c.loc[i,j] = min([x+y for x, y in zip(row, col)])
    
    return c

if __name__=='__main__':

    g = nx.DiGraph()
    
    g.add_weighted_edges_from(
        [
            ('b', 'a', 2),
            ('a', 'c', 3),
            ('b', 'd', 5),
            ('d', 'c', 4),
            ('c', 'b', 3),
        ]
    )

    h = nx.DiGraph()

    h.add_weighted_edges_from(
        [
            ('x', 'z', 3),
            ('z', 'y', 4),
            ('x', 'y', 4),
            ('y', 'x', 3),
        ]
    )

    phi = nx.union(g, h)

    phi.add_weighted_edges_from(
        [
            ('b', 'x', 11),
            ('d', 'y', 9),
        ]
    )

    mphi = pd.DataFrame(np.inf, index=g.nodes, columns=h.nodes)
    mphi.loc['b', 'x'] = 11
    mphi.loc['d', 'y'] = 9

    mx, my = map(one_step_distance_matrix, (g, h))
    mx3 = cost_mult(mx, cost_mult(mx, mx))
    my2 = cost_mult(my, my)

    total_dist = cost_mult(cost_mult(mx3,mphi),my2)