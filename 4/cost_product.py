"""
Categories enriched in quantales and profunctor multiplication.
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
class QMatrix:
    """
    Matrix with elements in a quantale.
    """

    def __init__(self, data, enrich, index=None, columns=None):

        if not hasattr(data, 'shape'):
            data = np.array(data)

        self._enrich = enrich
        self._data = self._wrap_data(data, index=index, columns=columns)
        self.index, self.columns = self._data.index, self._data.columns
        self.shape = self._data.shape

    def closure(self):
        return self ** self.shape[0] # TODO

    def __mul__(self, other):
        if isinstance(other, QMatrix):
            if other._enrich != self._enrich:
                raise TypeError("Cannot multiply {}-profunctor with {}-profunctor - they need to be enriched on the same category".format(self._enrich, other._enrich))
            _other = other
        else:
            _other = self.__class__(other, enrich=self._enrich)

        if other.shape[0] != self.shape[1]:
            raise ValueError('Incompatible dimensions {} and {}'.format(self.shape, _other.shape))

        new_data = [[sum([x*y for x, y in zip(row, col)], start=self._enrich._zero) for _, row in self._data.iterrows()] for _, col in _other._data.T.iterrows()]

        return self.__class__(
            data = new_data,
            enrich = self._enrich,
            index=self.index,
            columns=_other.columns
        )

    def __pow__(self, n): return reduce(lambda x, y: x*y, [self]*n)

    @property
    def zero(self):
        return self.__class__(
            data=np.full(self.shape, self._enrich._zero),
            enrich=self._enrich
        )

    @property
    def unit(self):
        one = np.full(self.shape, self._enrich._zero)
        np.fill_diagonal(one, self._enrich._unit) # inplace
        return self.__class__(
            data=one,
            enrich=self._enrich
        )

    def _wrap_data(self, data, index=None, columns=None):

        if isinstance(data, pd.DataFrame):
            iter_data = [row for _, row in data.iterrows()]
            idx = data.index if index is None else index
            cols = data.columns if columns is None else columns
        elif isinstance(data, np.ndarray):
            iter_data = data
            idx = list(range(data.shape[0])) if index is None else index
            cols = list(range(data.shape[1])) if columns is None else columns
        elif isinstance(data, list):
            iter_data = data
            idx = list(range(len(data))) if index is None else index
            cols = list(range(len(data[0]))) if columns is None else columns # TODO check all rows are same length

        return pd.DataFrame([[self._enrich._wrap(x) for x in row] for row in iter_data], index=idx, columns=cols)

    @classmethod
    def from_graph(cls, g, enrich):
        # TODO guess enrichment category based on attributes on g's edges
        return cls(
            data=cls.adj_matrix(g, enrich),
            enrich=enrich,
            index=g.nodes,
            columns=g.nodes
            )

    @classmethod
    def adj_matrix(cls, g, enrich):
        v = list(g.nodes)
        e = pd.DataFrame([[enrich._unit if k==j else enrich._zero for k in g.nodes] for j in g.nodes], index=v, columns=v)
        d = e.copy()

        for edge in g.edges:
            # TODO if g is not a digraph I want the adj matrix to be symmetric but this won't do it
            # there has to be a simpler way using a networkx method
            a, b = edge
            d.loc[a,b] = g.edges[edge].get('weight', True)

        return d

    def __repr__(self):
        return self._data.__repr__()

    def __str__(self):
        return self._data.__str__()

    # Helpers
    def _wrap(self, other):
        if isinstance(other, self.__class__):
            return other
        return self.__class__(data=other, enrich=self._enrich)

class Quantale:

    _unit = None # multiplicative unit
    _zero = None # additive unit

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
    def __mul__(self, other): raise NotImplementedError
    def __rmul__(self, other): return self._wrap(other) * self
    def hom(self, other): raise NotImplementedError
    def __pow__(self, n : int): return reduce(lambda x,y: x*y, [self.x]*n)
    @property
    def unit(self): return self._wrap(self._unit)
    
    # Addition
    def __add__(self, other):
        return self._join(other)

    def __radd__(self, other):
        return self._wrap(other)._join(self)

    @classmethod
    def join(cls, *args):
        """Join of all args."""
        # NB: if you do
        # > q = Quantale(x)
        # > j = q.join(y,z)
        # then j will be the join of y and z
        # This is expected behaviour: q is not available in this scope because this is a class method!
        return reduce(lambda x, y: x._join(y), map(cls._wrap, args))

    def _join(self, other):
        raise NotImplementedError
    
    @property
    def zero(self): return self._wrap(self._zero)

    # Printing
    def __repr__(self):
        return 'Quantale {} {}'.format(self._args, self._kwds)
    
    def __str__(self):
        return self.__repr__()
    
    # Helpers
    @classmethod
    def _wrap(cls, other):
        if isinstance(other, cls):
            return other
        return cls(other)

class Bool(Quantale):

    _unit = True
    _zero = False

    def __init__(self, x : bool):
        super().__init__()
        self._x = x

    # Preorder
    def __eq__(self, other): return self._x.__eq__(self._wrap(other)._x)
    def __le__(self, other): return self._x.__le__(self._wrap(other)._x)

    # Multiplication
    def __mul__(self, other): return self._wrap(self._x and self._wrap(other)._x)
    def hom(self, other): return self._wrap((not self._x) or self._wrap(other)._x)

    # Addition
    def _join(self, other): return self._wrap(self._x or self._wrap(other)._x)

    # Printing
    def __repr__(self): return 'Bool {}'.format(self._x)

class Cost(Quantale):

    _unit = 0
    _zero = np.inf

    def __init__(self, x : np.float):
        self._x = x

    # Preorder
    def __eq__(self, other): return self._x.__eq__(self._wrap(other)._x)
    def __le__(self, other): return self._x.__le__(self._wrap(other)._x)

    # Multiplication
    def __mul__(self, other): return self._wrap(self._x + self._wrap(other)._x)
    def hom(self, other): return self._wrap(self._wrap(other)._x - self._x)

    # Addition
    def _join(self, other):
        return self._wrap(min(self._x, self._wrap(other)._x))

    # Printing
    def __repr__(self): return 'Cost {}'.format(self._x)

    
def one_step_distance_matrix(g, enrich):
    v = list(g.nodes)
    e = pd.DataFrame([[enrich._unit if k==j else enrich._zero for k in g.nodes] for j in g.nodes], index=v, columns=v)
    d = e.copy()

    for edge in g.edges:
        a, b = edge
        d.loc[a,b] = g.edges[edge].get('weight', True)

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

    # mphi = pd.DataFrame(np.inf, index=g.nodes, columns=h.nodes)
    # mphi.loc['b', 'x'] = 11
    # mphi.loc['d', 'y'] = 9

    # mx, my = map(one_step_distance_matrix, (g, h))
    # mx3 = cost_mult(mx, cost_mult(mx, mx))
    # my2 = cost_mult(my, my)

    # total_dist = cost_mult(cost_mult(mx3,mphi),my2)

    # With profunctors
    Pphi = QMatrix.from_graph(phi, Cost)

    try:
        print(Pphi*Pphi)
    except:
        raise
        #print('fail')