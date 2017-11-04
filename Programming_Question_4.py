from collections import defaultdict
from collections import OrderedDict
import pickle
# -*- coding: utf-8 -*-
'''
The file contains the edges of a directed graph. Vertices are labeled as positive integers from 1 to 875714. Every row indicates an edge, the vertex label in first column is the tail and the vertex label in second column is the head (recall the graph is directed, and the edges are directed from the first column vertex to the second column vertex). So for example, the 11th row looks liks : "2 47646". This just means that the vertex with label 2 has an outgoing edge to the vertex with label 47646

Your task is to code up the algorithm from the video lectures for computing strongly connected components (SCCs), and to run this algorithm on the given graph.

Output Format: You should output the sizes of the 5 largest SCCs in the given graph, in decreasing order of sizes, separated by commas (avoid any spaces). So if your algorithm computes the sizes of the five largest SCCs to be 500, 400, 300, 200 and 100, then your answer should be "500,400,300,200,100" (without the quotes). If your algorithm finds less than 5 SCCs, then write 0 for the remaining terms. Thus, if your algorithm computes only 3 SCCs whose sizes are 400, 300, and 100, then your answer should be "400,300,100,0,0" (without the quotes). (Note also that your answer should not have any spaces in it.)

WARNING: This is the most challenging programming assignment of the course. Because of the size of the graph you may have to manage memory carefully. The best way to do this depends on your programming language and environment, and we strongly suggest that you exchange tips for doing this on the discussion forums.
'''

def innerInvertedDFS(graph, visited, start, finishTime, T):
    stack = [start]
    while stack:
        vertex = stack.pop()
        if vertex not in visited:
            visited.add(vertex)
            stack.append(vertex)
            stack.extend(graph[vertex] - visited)
        else:
            if vertex not in finishTime.keys():
                finishTime[vertex] = T
                T += 1
    return visited, finishTime


def innerDFS(graph, visited, start, leaders):
    stack = [start]
    leaders[start] = set()
    while stack:
        vertex = stack.pop()
        if vertex not in visited:
            visited.add(vertex)
            stack.extend(graph[vertex] - visited)
        leaders[start].add(vertex)
    return visited, leaders


def outerDFS(graph):
    finishTime = OrderedDict()
    visited = set()
    T = 0  # count how many nodes we've finished exploring at this point
    mainGraph = graph[0]
    reversedGraph = graph[1]
    for vertex in range(1, max(max(item) for item in reversedGraph.values() if item)):
        if vertex not in visited:
            visited, finishTime = innerInvertedDFS(reversedGraph, visited, vertex, finishTime, T)
    visited = set()
    leaders = defaultdict(set)
    for vertex in reversed(list(finishTime.keys())):
        if vertex not in visited:

            visited, leaders = innerDFS(mainGraph,visited, vertex, leaders)
    print(generateAnswer(leaders))


def generateAnswer(leaders):
    answer = []
    for v in sorted(leaders.values(), key=lambda v: len(v)):
        answer.append(len(v))
    answer = answer[::-1]
    if len(answer) > 5:
        answer = answer[:5]
    else:
        answer += [0] * (5 - len(answer))
    return ','.join([str(item) for item in answer])


def main():

    # Load graph from file
    def generateGraph():
        with open('SCC.txt') as file:
            maximum = 875714
            currentGraph, currentReverseGraph = defaultdict(set), defaultdict(set)
            for i in range(1, maximum+1):
                currentGraph[i] = set()
                currentReverseGraph[i] = set()
            for line in file:
                tail, head = line.split()
                currentGraph[int(tail)].add(int(head))
                currentReverseGraph[int(head)].add(int(tail))
        return currentGraph, currentReverseGraph

    def serializeGraphs(graph, invertedGraph):
        with open('graph.pickle', 'wb') as handle:
            pickle.dump((graph, invertedGraph), handle,
                        protocol=pickle.HIGHEST_PROTOCOL)

    def deSerializeGraphs(filename):
        with open('graph.pickle', 'rb') as handle:
            graph, invertedGraph = pickle.load(handle)
        return graph, invertedGraph

    def generateTestGraphs():
        graphs = [['1 4', '2 8', '3 6', '4 7', '5 2', '6 9', '7 1', '8 5', '8 6', '9 7', '9 3'],
                  ['1 2', '2 3', '2 4', '2 5', '3 6', '4 5', '4 7', '5 2', '5 6', '5 7', '6 3',
                      '6 8', '7 8', '7 10', '8 7', '9 7', '10 9', '10 11', '11 12', '12 10'],
                  ['1 2', '2 6', '2 3', '2 4', '3 1', '3 4', '4 5', '5 4', '6 5', '6 7', '7 6', '7 8', '8 5', '8 7'],
                  ['1 2','2 3','3 1','3 4','5 4','6 4','8 6','6 7','7 8'],
                  ['1 2','2 3','3 1','3 4','5 4','6 4','8 6','6 7','7 8','4 3','4 6']]
        testGraphs = []
        for graph in graphs:
            maximum = max([int(number) for item in graph for number in item.split()])
            currentGraph, currentReverseGraph = defaultdict(set), defaultdict(set)
            for i in range(1, maximum+1):
                currentGraph[i] = set()
                currentReverseGraph[i] = set()
            for item in graph:
                tail, head = item.split()
                currentGraph[int(tail)].add(int(head))
                currentReverseGraph[int(head)].add(int(tail))
            testGraphs.append((currentGraph, currentReverseGraph))
        return testGraphs

    # Run tests
    # testGraphs = generateTestGraphs()
    # for graph in testGraphs:
    #     # if testGraphs.index(graph) == 3:
    #     outerDFS(graph)
    # print('answers: 3,3,3,0,0 and 6,3,2,1,0 and 3,3,2,0,0 and 3,3,1,1,0 and 7,1,0,0,0')

    # Load graph and calculate SCC's
    # graph, invertedGraph = generateGraph()
    # serializeGraphs(graph, invertedGraph)
    graph, invertedGraph = deSerializeGraphs('graph.pickle')
    outerDFS((graph, invertedGraph))


if __name__ == '__main__':
    main()
