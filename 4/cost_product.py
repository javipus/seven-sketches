"""
Matrix multiplication in Cost-categories.
"""
from functools import reduce
import numpy as np
import pandas as pd
import networkx as nx

# TODO
# class Quantale
# class Profunctor
#   def __mult__

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