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

graph1 = {
    "1":[ ],
    "2":["1"],
    "3":["2"],
    "4":["2"],
    "5":["2", "3", "4"],
    "6":["5"],
    "7":["4"]
}
graph2 = {
    "1":[ ],
    "2":["1", "4"],
    "3":["2"],
    "4":["7"],
    "5":["2", "3", "4"],
    "6":["5"],
    "7":[ ]
}
print("Graph 1 without reversed:")
print(*topoLogicalPath(graph1, reverse=False))
print("\nGraph 1 with reversed:")
print(*topoLogicalPath(graph1, reverse=True))
print("\nGraph 2 without reversed:")
print(*topoLogicalPath(graph2, reverse=False))
print("\nGraph 2 with reversed:")
print(*topoLogicalPath(graph2, reverse=True))
