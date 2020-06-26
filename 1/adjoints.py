import copy
from functools import reduce

import numpy as np

class Diagram:

    def __init__(self, data):
        """
        `data` is a list of 3-tuples (x,y,f) with:
            x :: Set is the domain object
            y :: Set is the codomain object
            f :: x -> y is an arrow
        """

        self._data = data
        self.points = set(reduce(lambda x,y: x+y, map(lambda item: [item[0], item[1]], self._data)))
        self.arrows = [f for (x,y,f) in self._data]

class Limit:

    def __init__(self, diagram):
        self._diagram = diagram

class PushoutAdjoints(Limit):
    """
    Pushout blabla TODO
    """

    def __init__(self, x, y, f):
        self.x = x
        self.y = y
        self.f = f

        self._cache = {xx: f(xx) for xx in x}
        self._preim = {yy: set() for yy in self.y}

        for xx, yy in self._cache.items():
            self._preim[yy].add(xx)

        #super(PushoutAdjoints, self).__init__(Diagram([(self.x, self.y, self.f)]))

    def left(self, c):
        """
        Left adjoint f! :: Prt x -> Prt y.
        c :: x -> classes_x must induce a partition on x.
        """
        # get the class of each element in the pre-image of each y
        cl = [set(map(c, self._preim[yy])) for yy in self.y]

        # Transitive closure
        # for each class, check if it belongs to a larger class and drop it if that's the case
        cl = [s for s in cl if not any([s.issubset(t) for t in cl if s!=t])]
        
        # define g_star handling case when f is not surjective
        def g_star(yy):
            # handle non-surjective
            if not (xx:=self._preim[yy]):
                return yy
            else:
                cx = list(np.unique([s for s in cl if c(copy.copy(xx).pop()) in s]))
                assert len(cx) == 1, "More than one class for {}".format(xx)
                return cx[0]

        return g_star

    def right(self, c):
        """
        Right adjoint f* :: Prt y -> Prt x.
        c :: y -> classes_y must induce a partition on y.
        """
        def g_bang(xx):
            try:
                return c(self.f(xx))
            except KeyError:
                raise TypeError("Point {} not in domain {}!".format(xx, self.x))
        return g_bang

class PullbackAdjoints(Limit):
    """
    Pullback of a function and its left and right adjoints in FinSet.

    This implementation follows from the exposition in Seven Sketches, Example 1.117.
    """

    def __init__(self, x, y, f):
        """
        @param x: domain
        @param y: codomain
        @param f: f:x->y
        """
        self.x = x
        self.y = y
        self.f = f

        self._cache = {xx: f(xx) for xx in x}
        self._preim = {yy: set() for yy in self.y}

        for xx, yy in self._cache.items():
            self._preim[yy].add(xx)

    def _union(self, sets):
        return reduce(lambda x, y: x.union(y), sets)

    def pullback(self, ys):
        return self._union([self._preim[yy] for yy in ys])

    def left(self, xs):
        return self._union([set([self._cache[xx]]) for xx in xs])

    def right(self, xs):
        return set([yy for yy in self.y if self._preim[yy].issubset(set(xs))])

def problem118():
    x = list(range(4))
    y = True, False
    f = lambda xx: xx%2==0

    b1 = set([True])
    b2 = set([False])
    
    a1 = set([0,2])
    a2 = set([1,2])

    pb = PullbackAdjoints(x,y,f)
    
    print('\n')
    print('Pullbacks:')
    print('f* {} = {}'.format(b1, pb.pullback(b1)))
    print('f* {} = {}'.format(b2, pb.pullback(b2)))
    
    print('\n')
    print('Left adjoints:')
    print('f! {} = {}'.format(a1, pb.left(a1)))
    print('f! {} = {}'.format(a2, pb.left(a2)))
    
    print('\n')
    print('Right adjoints:')
    print('f_* {} = {}'.format(a1, pb.right(a1)))
    print('f_* {} = {}'.format(a2, pb.right(a2)))

if __name__=='__main__':

    x = [1, 2, 3, 4, 5]
    y = ['a', 'b', 'c', 'd', 'e', 'f']
    f = {1: 'b', 2: 'a', 3: 'c', 4: 'e', 5: 'd'}

    cx = lambda xx: xx%2
    cy = lambda yy: 0 if yy in ('a', 'e', 'i', 'o', 'u') else 1

    po = PushoutAdjoints(x, y, lambda k: f[k])
    pb = PullbackAdjoints(x, y, lambda k: f[k])

    problem118()