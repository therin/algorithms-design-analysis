from collections import defaultdict
import pickle
# -*- coding: utf-8 -*-
'''
No recursion due to depth limit
Use defaultdict to store linked list, instead of list, use set
no need to use class for vertices to add properties (discover time, finish time, color, etc), use dict
append no insert

The file contains the edges of a directed graph. Vertices are labeled as positive integers from 1 to 875714. Every row indicates an edge, the vertex label in first column is the tail and the vertex label in second column is the head (recall the graph is directed, and the edges are directed from the first column vertex to the second column vertex). So for example, the 11th row looks liks : "2 47646". This just means that the vertex with label 2 has an outgoing edge to the vertex with label 47646

Your task is to code up the algorithm from the video lectures for computing strongly connected components (SCCs), and to run this algorithm on the given graph.

Output Format: You should output the sizes of the 5 largest SCCs in the given graph, in decreasing order of sizes, separated by commas (avoid any spaces). So if your algorithm computes the sizes of the five largest SCCs to be 500, 400, 300, 200 and 100, then your answer should be "500,400,300,200,100" (without the quotes). If your algorithm finds less than 5 SCCs, then write 0 for the remaining terms. Thus, if your algorithm computes only 3 SCCs whose sizes are 400, 300, and 100, then your answer should be "400,300,100,0,0" (without the quotes). (Note also that your answer should not have any spaces in it.)

WARNING: This is the most challenging programming assignment of the course. Because of the size of the graph you may have to manage memory carefully. The best way to do this depends on your programming language and environment, and we strongly suggest that you exchange tips for doing this on the discussion forums.
'''

# Load graph from file
def generateGraph():
    with open('SCC.txt') as file:
        graph = defaultdict(list)
        for line in file:
            # print(line.strip().split(' '))
            graph[line.strip().split(' ')[0]].append(line.strip().split(' ')[1])
    return graph

# Serialaze graph object to file for faster load time
# graph = generateGraph()
# with open('graph.pickle', 'wb') as handle:
#     pickle.dump(graph, handle, protocol=pickle.HIGHEST_PROTOCOL)

with open('graph.pickle', 'rb') as handle:
    fast = pickle.load(handle)

print(fast['11'])

