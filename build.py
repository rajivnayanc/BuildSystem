import os
import json

def topoUtil(graph, visited, curr_node, topo):
    visited[curr_node] = True
    for node in graph[curr_node]:
        if visited[node]==False:
            topoUtil(graph,visited, node, topo)
    topo.append(curr_node)
    
def topoLogicalPath(graph, reverse=False):
    topo = [] # List to store topological Order
    visited = {node:False for node in graph.keys()}
    KEYS = list(graph.keys())
    if reverse:
        KEYS = KEYS[::-1]
    for node in KEYS:
        if visited[node]==False:
            topoUtil(graph, visited, node, topo)
    return topo[::-1] # reverse the list and return

f = open("build.json", "r")
bSystem = json.load(f)
graph = {key:[] for key in bSystem.keys()}
for key, value in bSystem.items():
    for pNode in value["dep"]:
        graph[pNode].append(key)
topoSorted = topoLogicalPath(graph)
for echo in [bSystem[node]["cmd"] for node in topoSorted]:
    os.system(echo)