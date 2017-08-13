def findAllPaths(graph,start,end,path=[]):
    path = path + [start]
    if start == end: return [path]
    if not graph.has_key(start): return []
    paths = []
    for node in graph[start]:
        if node not in path:
            new_paths = findAllPaths(graph, node, end, path)
            for new_path in new_paths:
                paths.append(new_path)
    return paths
    
    
    