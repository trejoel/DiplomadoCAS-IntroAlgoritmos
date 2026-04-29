#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jan 27 17:37:58 2022

@author: cimat
"""

#!/usr/bin/python
import networkx as nx
import random
import matplotlib.pyplot as plt



#Random graph with N vertices, with probability (0,1) to connect two given vertices
def generateRandomGraph(N,P):
    G=nx.gnp_random_graph(N,P)
    while (nx.is_connected(G)==False):
        G=nx.gnp_random_graph(N,P)
    return G
    

def writeGraph(G,str):
    nx.write_gml(G,str)


def isVertexCover(G,candidate):
    edges=list(G.edges)
    for xEdge in edges:
        if (xEdge[0] not in candidate and xEdge[1] not in candidate):
            return False
    return True

def power_set(A):
    """A is an iterable (list, tuple, set, str, etc)
    returns a set which is the power set of A."""
    length = len(A)
    l = [a for a in A]
    ps = set()

    for i in range(2 ** length):
        selector = f'{i:0{length}b}'
        subset = {l[j] for j, bit in enumerate(selector) if bit == '1'}
        ps.add(frozenset(subset))
    return ps

def minimumVertexCover(G):
    minVertexCover=list(G.nodes)
    minCardinality=len(G.nodes)
    pS=power_set(list(G.nodes))
    candidates=[list(x) for x in pS]
    for candidate in candidates:
        if (isVertexCover(G,candidate)):
            if (len(minVertexCover)>len(candidate)):
                minVertexCover=candidate
    return minVertexCover

def TwoAppVertexCover(G):
    H=set()
    edges = list(G.edges)
    while (len(edges)>0): 
        chosen_edge = random.choice(edges)
        H.add(chosen_edge[0])
        H.add(chosen_edge[1])
        edges=list(filter(lambda x: (x[0]!=chosen_edge[0] and x[0]!=chosen_edge[1] and x[1]!=chosen_edge[0] and x[1]!=chosen_edge[1]),edges))
    return H


if __name__ == '__main__':
    G=generateRandomGraph(15,0.2)
    #G=nx.minimum_spanning_tree(G)
    H=TwoAppVertexCover(G)
    color_map=[]
    for node in G:
        if node in H:
            color_map.append('red')
        else:
            color_map.append('blue')
    nx.draw(G,node_color=color_map,with_labels="true")
    plt.show()
    print("Vertex Cover:",H)
    HOpt=minimumVertexCover(G)
    color_map=[]
    for node in G:
        if node in HOpt:
            color_map.append('yellow')
        else:
            color_map.append('blue')
    nx.draw(G,node_color=color_map,with_labels="true")
    plt.show()
    print("Min Vertex Cover",HOpt)