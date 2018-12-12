# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

from Weighted_Graph import *

G = Weighted_Graph('test_graph.txt')

#print(G.edge_dict())
#print(G.edge_set())
#print(G.vertex_set())
#G.draw_graph()

#H = ({0, 1, 3}, [(0,1),(1,3)])


def c(e,G):
    return G.edge_dict()[e]

#T = ({2, 3, 5},[(2, 3),(2, 5)])
 
def incident_edges(T,G):
    edges = []
    for v in T[0]:
        for e in G.edge_set():
            if v in e and e not in edges:
                edges.append(e)
        for e in edges:
            if e in T[1]:
                edges.remove(e)          
    return edges

#G.draw_subgraph(T)
#print(incident_edges(T,G))
#print(T)

def valid_edges(T, G):
    edges = incident_edges(T,G)
    notvalid = incident_edges(T,G)
    vlist = G.vertex_set().difference(set(T[0]))
    for v in T[0]:
        for x in vlist:
            for e in G.edge_set():
                if v in e and x in e and e in edges:
                    notvalid.remove(e)
    edges = list(set(edges) - set(notvalid))
    return edges      


def min_valid_edges(T,G):
    edges = valid_edges(T, G)
    min_edges = edges[0]     
    for e in edges:
        if (c(e,G)) < c(min_edges,G):
            min_edges = e
    return min_edges

def update(T,G):
    vertices = set(T[0])
    edges = list(T[1])
    update = min_valid_edges(T,G)
    edges.append(update)
    for v in update:
        if v in G.vertex_set() and v not in vertices:
            vertices.add(v)
    T2 = [vertices, edges]
    return T2

def total_sum(T, G):
    return sum([c(e,G) for e in T[1]])