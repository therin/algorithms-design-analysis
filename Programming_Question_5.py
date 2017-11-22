# -*- coding: utf-8 -*-
from collections import defaultdict

'''
The file contains an adjacency list representation of an undirected weighted graph with 200 vertices labeled 1 to 200.
Each row consists of the node tuples that are adjacent to that particular vertex along with the length of that edge. For example,
the 6th row has 6 as the first entry indicating that this row corresponds to the vertex labeled 6. The next entry of this row "141,8200" indicates
that there is an edge between vertex 6 and vertex 141 that has length 8200. The rest of the pairs of this row indicate the other vertices adjacent
 to vertex 6 and the lengths of the corresponding edges.

Your task is to run Dijkstra's shortest-path algorithm on this graph, using 1 (the first vertex) as the source vertex, and to compute the shortest-path
distances between 1 and every other vertex of the graph. If there is no path between a vertex v and vertex 1, we'll define the shortest-path distance
between 1 and v to be 1000000.

You should report the shortest-path distances to the following ten vertices, in order: 7,37,59,82,99,115,133,165,188,197. You should encode the
 distances as a comma-separated string of integers. So if you find that all ten of these vertices except 115 are at distance 1000 away from vertex 1
  and 115 is 2000 distance away, then your answer should be 1000,1000,1000,1000,1000,2000,1000,1000,1000,1000. Remember the order of reporting DOES
  MATTER, and the string should be in the same order in which the above ten vertices are given. The string should not contain any spaces. Please type
   your answer in the space provided.

IMPLEMENTATION NOTES: This graph is small enough that the straightforward O(mn) time implementation of Dijkstra's algorithm should work fine.
 OPTIONAL: For those of you seeking an additional challenge, try implementing the heap-based version. Note this requires a heap that supports deletions,
  and you'll probably need to maintain some kind of mapping between vertices and their positions in the heap.


Dijkstra’s Algorithm: (computing distances from source vertex S to every other vertex)
- X (list of conquered vertices, with path computed from source vertex S to every vertex of X) = [S] [starting node]. This is updated with each iteration
of main loop
- A[s] = 0 [computed  shortest path distances - goal of the algorithms - answer]
- B[s] store actual path (only to help explanation)
note: each iteration will grow X by one vertex, like a mould
main loop:
while X != V (list of unprocessed vertices):
- search (scan) for vertices whose tail are among vertices in X and head in (V-X, not yet explored). Remember this is a directed graph;
- give each vertex a score based on how close it is to the source vertex S and then pick among all candidates the one with minimal score.
Following formula is used: Shortest path distance that we previously computed from S to the vertex V, denoted as A[r] + length of the edge
that connects the edge V to W (W is our new vertex we are scoring). This is called Dijkstra Greedy Criterion. We denote the best path as (V*,W*)
- add W* to X
- set A[W*] = A[V*] + Dijkstra Greedy Criterion [V*,W*]
- set B[W*] = B[v*] + (union) (v*, w*)
- profit!

Key for heap in Dijkstra: key[vertex] = smallest greedy d score of any edge that has this vertex as its head
Think of it as of tournaments:
- local: out of all neighbours for X run a local tournament for lowest DGC and only remember winner in a heap
- extract min from the heap to get a winner W*

Think about:
every time you move W to X from V-X, edges sticking out of W must be rebalanced as they may have created lower DGC scores:
for each edge (w,v):
- if head of this edge is still in the heap (V-X):
    - update it’s key (rip it out of the heap, recompute it’s key to key[v] = min and insert back)
    - make sure it’s not a new winner in min[key[v], A[W] + &wv]
'''


def findScoreCrossingVertices(X, V, A, currentCrossingVertices):
    for vertex in X.keys():
        print(f'testing vertex {vertex}')
        for neighbour in V[vertex]:
            if neighbour[0] not in X.keys():
                # calculate score for found vertex
                score = A[vertex] + neighbour[1]
                print(f'calculated {neighbour[0]} score as {A[vertex]} + {neighbour[1]}')
                # update distance dictionary
                if neighbour[0] not in A.keys():
                    A[neighbour[0]] = score
                if A[neighbour[0]] > score:
                    A[neighbour[0]] = score
                currentCrossingVertices.add((neighbour[0], score))
    toReturn = {k: v for k, v in A.items() if k in [
        item[0] for item in currentCrossingVertices] and k not in X.keys()}
    bestNode = sorted(toReturn.items(), key=lambda x: x[1])[0]
    return bestNode


def dijkstra(connections):
    currentCrossingVertices = set()
    tempCounter = 0
    S = 1
    V = connections
    X = defaultdict(set)
    A = defaultdict(int)
    X[S] = set()
    A[S] = 0
    while X.keys() != V.keys():
        closestVertex = findScoreCrossingVertices(
            X, V, A, currentCrossingVertices)
        print(f'node {closestVertex[0]} is closer to S with a distance of {closestVertex[1]}, adding it to X')
        X[closestVertex[0]] = 0
        print(f'current X is {X}')
        tempCounter += 1
        print(f'current A is: {A}')
    return A


if __name__ == '__main__':
    # Load graph from file
    connections = defaultdict(set)

    def generateGraph():
        with open('dijkstraData.txt') as file:
            for line in file:
                currentVertex = int(line.split()[0])
                connections[currentVertex] = [(int(connection.split(',')[0]), int(
                    connection.split(',')[1])) for connection in line.split()[1:]]
        return True

    generateGraph()
    # 2599,2610,2947,2052,2367,2399,2029,2442,2505,3068 - CORRECT
    print(connections)
    A = dijkstra(connections)
    # print answer
    print(','.join([str(i) for i in [A[7], A[37], A[59], A[82], A[99], A[
          115], A[133], A[165], A[188], A[197]]]))
