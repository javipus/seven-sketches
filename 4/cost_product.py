"""
Matrix multiplication in Cost-categories.
"""

import numpy as np
import pandas as pd
import networkx as nx

def distance_matrix(g):
    n = g.number_of_nodes
    v = list(g.nodes)
    d = pd.DataFrame(np.inf, index=v, columns=v)

    for edge in g.edges:
        d[a,b] = edge.weight

    d = pd.DataFrame(reduce(lambda x,y: x@y, [d.values]*n), index=v, columns=v)

    return d

def cost_mult(a, b):
    """

    Args:
        a ([type]): [description]
        b ([type]): [description]
    """

    c = np.zeros((a.shape[0], b.shape[1]))

    for i, row in a.iterrows():
        for j, col in b.T.iterrows():
            c[i,j] = sum([min(x,y) for x, y in zip(row, col)])
    
    return c

if __name__=='__main__':

    g = nx.Graph()
    # TODO example