import random
import copy
from statistics import mode
# -*- coding: utf-8 -*-
'''
The file contains the adjacency list representation of a simple undirected graph. There are 200 vertices
labeled 1 to 200.
 The first column in the file represents the vertex label, and the particular row (other entries except
 the first column)
 tells all the vertices that the vertex is adjacent to. So for example, the 6th row looks like : "6 155 56
 52  120 ......".
  This just means that the vertex with label 6 is adjacent to (i.e., shares an edge with) the vertices with
  labels
  155,56,52,120,......,etc
Your task is to code up and run the randomized contraction algorithm for the min cut problem and use it on the
above
graph to compute the min cut. (HINT: Note that you'll have to figure out an implementation of edge contractions.
Initially, you might want to do this naively, creating a new graph from the old every time there's an edge
 contraction.
 But you should also think about more efficient implementations.) (WARNING: As per the video lectures, please
 make sure
 to run the algorithm many times with different random seeds, and remember the smallest cut that you ever find.)
 Write your numeric answer in the space provided. So e.g., if your answer is 5, just type 5 in the
 space provided.
I can't provide the test case for you. Think of the possible scenarios. There are two inputs and three possible
 outcomes depending on >,<, or =. Have you account for all the options. Hope this helps.

Ingridients:
- list of vertices
- list of edges
- each edge pointers to its endpoint
- each vertex point to all edges incident on it

Karger Algorithm:
while there are more than 2 vertices:
- pick a remaining edge randomly
- take 2 vertex u/v and merge them into single vertex
- remove self-loops
return the cut represented by 2 final vertices
'''

class Node():

    def __init__(self, ida):
        self.ida = ida
        self.edges = []


class Graph():

    def __init__(self, nodes=None):
        self.status = "cool"
        self.nodes = []

    def addEdge(self, node1, node2):
        node1.edges.append(node2)

    def addNode(self, ida):
        if ida not in self.getNodesIds():
            new_node = Node(ida)
            self.nodes.append(new_node)

    def chooseRandomEdge(self):
        one = random.choice(self.nodes)
        two = random.choice(one.edges)
        return one, two

    def getNodesIds(self):
        return [node.ida for node in self.nodes]

    def getNodeById(self, id):
        for node in self.nodes:
            if node.ida == id:
                return node


def generateGraph():
    with open('kargerMinCut.txt') as file:
        graph = Graph()
        for line in file:
            graph.addNode(line.strip().split('\t')[0])
            for i in line.strip().split('\t')[1:]:
                graph.addNode(i)
                graph.addEdge(graph.getNodeById(line.strip().split('\t')[0]), graph.getNodeById(i))
    return graph


def kargerAssimilate(graph):
    one, two = graph.chooseRandomEdge()
    #  merge 2 into 1 and delete 2 from graph
    two.edges = one.edges + two.edges
    graph.nodes.remove(one)
    #  replace all occurences of 1 from graph with 2
    for node in graph.nodes:
        node.edges = [edge if edge != one else two for edge in node.edges]
    two.edges = [edge for edge in two.edges if edge != two]
    return graph

results = []
currentGraph = generateGraph()

for i in range(1, 100):
    currentGraph = generateGraph()
    print(len(currentGraph.nodes))
    while len(currentGraph.nodes) > 2:
        # print(len(currentGraph.nodes))
        kargerAssimilate(currentGraph)
    results.append(max([len(node.edges) for node in currentGraph.nodes]))

print(sorted(results))
