class Object:

    def __init__(self, *args, **kwds):
        self._args = args
        self._kwds = kwds

    def __eq__(self, value):
        return (self._args).__eq__(value._args) and\
            (self._kwds).__eq__(value._kwds)

class Arrow:

    def __init__(self, dom : Object, cod : Object, *args, **kwds):
        if not isinstance(dom, Object):
            dom = Object(dom)
        if not isinstance(cod, Object):
            cod = Object(cod)

        self._dom = dom
        self._cod = cod
        self._args = args
        self._kwds = kwds

class Diagram:

    def __init__(self, objects, morphisms):
        self.obj = objects
        self.arr = morphisms

class Span(Diagram):

    def __init__(self, objects, morphisms):
        a, b, c = objects
        f, g = morphisms
        assert f._dom == b
        assert f._cod == a
        assert g._dom == b
        assert g._cod == c
        super().__init__(objects, morphisms)

class Limit:
    def __init__(self, diagram):
        self._diagram = diagram

class Colimit:
    def __init__(self, diagram):
        self._diagram = diagram

class Pushout(Colimit):

    def __init__(self, diagram : Span = None):
        if diagram is None:
            diagram = Span(
                objects=map(Object, ('a', 'b', 'c')),
                morphisms=(Arrow('b', 'a', 'f'), Arrow('b', 'c', 'g'))
            )
        assert isinstance(diagram, Span)
        super().__init__(diagram=diagram)

    @classmethod
    def from_data(cls, a, b, c, f, g):
        objects = map(Object, (a, b, c))
        arrows = map(Arrow, (f, g))
        diagram = Span(objects, arrows)
        return cls(diagram)

    def get(self, sets, functions):
        a, b, c = sets
        assert all(map(lambda x: isinstance(x, set), (a, b, c)))

        f, g = functions
        assert all(map(lambda x: hasattr(x, '__call__'), (f, g)))

        R = {}

        for aa in a:
            for cc in c:
                if any([f(bb)==aa and g(bb)==cc for bb in b]):
                    R[(aa, cc)] = True
                else:
                    R[(aa, cc)] = False

        return R

def disjoint_union(a, b):
    a1 = set([(aa, 1) for aa in a])
    b2 = set([(bb, 2) for bb in b])
    return a1.union(b2)

if __name__=='__main__':

    a = set([1, 2, 3, 4, 5])
    b = set([1, 2, 3, 4])
    c = set([1, 2, 3])

    fd = {1: 1, 2: 1, 3: 3, 4: 5}
    gd = {1: 1, 2: 2, 3: 3, 4: 3}
        
    sets = a, b, c

    f = lambda x: fd[x]
    g = lambda x: gd[x]
    
    funcs = f, g

    p = Pushout()

    R = p.get(sets, funcs)