import random
import copy
# -*- coding: utf-8 -*-
'''
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

