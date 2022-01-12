import matplotlib.pyplot as plt
import networkx as nx
import numpy as np


def netList2Topo(matrix, names):
    topo = nx.Graph()
    n = len(matrix)
    for i in range(n):
        topo.add_node(names[i])

    for i in range(n):
        for j in range(n):
            if i != j and matrix[i][j] == 1:
                topo.add_edge(names[i], names[j])

    topo.name = 'netlist'

    return topo