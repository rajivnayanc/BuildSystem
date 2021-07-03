def dfsUtil(graph, visited, curr_node):
    visited[curr_node] = True
    print(curr_node, end=' ')
    for node in graph[curr_node]:
        if visited[node]==False:
            dfsUtil(graph,visited, node)
    
def dfs(graph, reverse=False):
    visited = {node:False for node in graph.keys()}
    KEYS = list(graph.keys())
    if reverse:
        KEYS = KEYS[::-1]
    for key in KEYS:
        if visited[key]==False:
            dfsUtil(graph, visited, key)


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
dfs(graph1, reverse=False)
print("\nGraph 1 with reversed:")
dfs(graph1, reverse=True)
print("\nGraph 2 without reversed:")
dfs(graph2, reverse=False)
print("\nGraph 2 with reversed:")
dfs(graph2, reverse=True)
