def dfs(graph):
    root = graph[0]
    visited, stack = set(), [root]
    while stack:
        vertex = stack.pop()
        if vertex not in visited:
            visited.add(vertex)
            stack.extend(graph[vertex] - visited)
    return visited

def depth_first_search_recursive(graph, start, visited=None):
    if visited is None:
        visited = set()
    visited.add(start)
    for next in graph[start] - visited:
        depth_first_search_recursive(graph, next, visited)
    return visited

a, b, c, d, e, f  = range(6)
input = [{b, c}, {d, e}, {f}]
print(dfs(input))
                