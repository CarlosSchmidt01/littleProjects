#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the findShortest function below.

#
# For the weighted graph, <name>:
#
# 1. The number of nodes is <name>_nodes.
# 2. The number of edges is <name>_edges.
# 3. An edge exists between <name>_from[i] to <name>_to[i].
#
#
def findShortest(graph_nodes, graph_from, graph_to, ids, val):
    # solve here
    graph = {}
    visited = []
    queue = []
    colors = {}
    founded = {}
    for con in zip(graph_from, graph_to):
        graph[con[0]] = [con[1]] if con[0] not in graph else graph[con[0]] + [con[1],]
        graph[con[1]] = [con[0]] if con[1] not in graph else graph[con[1]] + [con[0],]

    min_cs = -1

    for i in range(len(ids)):
        colors[i+1] = ids[i]

    def dfs(graph, start = 1, val):
        visited, stack = set(), [start]
        while stack:
            vertex = stack.pop()
            if vertex not in visited:
                visited.add(vertex)
                stack.extend(graph[vertex])
                if 
        return visited


    print(dfs(graph, val))
    '''
    while q and not end:
        n = q.pop()
        for nbour in graph[n]:
            print(nbour)
            if nbour in visited:
                if visited[n] == visited[nbour]:
                    min_cs = visited[nbour] * 2 + 1 if min_cs == -1 else min(visited[nbour] * 2 + 1, min_cs)
                if visited[n] + 1 == visited[nbour]:
                    min_cs = visited[nbour] * 2 if min_cs == -1 else min(visited[nbour] * 2, min_cs)
                end = True
            else:
                q.append(nbour)
                visited[nbour] = visited[n] + 1'''






if __name__ == '__main__':
    #fptr = open(os.environ['OUTPUT_PATH'], 'w')

    graph_nodes, graph_edges = map(int, input().split())

    graph_from = [0] * graph_edges
    graph_to = [0] * graph_edges

    for i in range(graph_edges):
        graph_from[i], graph_to[i] = map(int, input().split())

    ids = list(map(int, input().rstrip().split()))

    val = int(input())

    ans = findShortest(graph_nodes, graph_from, graph_to, ids, val)

    print(ans)
    #fptr.write(str(ans) + '\n')

    #fptr.close()
