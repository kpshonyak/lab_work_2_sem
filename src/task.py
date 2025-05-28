def read_graph(filename):
    with open(filename, 'r') as f:
        lines = [line.strip() for line in f if line.strip()]
    root = int(lines[0])
    edges = [line.split(',') for line in lines[1:]]

    graph = {}
    for u_str, v_str in edges:
        u, v = int(u_str), int(v_str)
        if u not in graph:
            graph[u] = []
        graph[u].append(v)
    return root, graph

def find_min_depth(root, graph):
    queue = [(root, 1, [root])]  
    min_depth = None
    min_path = []

    while queue:
        node, depth, path = queue.pop(0)  
        if node not in graph or len(graph[node]) == 0:
            if min_depth is None or depth < min_depth:
                min_depth = depth
                min_path = path
        else:
            for neighbor in graph[node]:
                queue.append((neighbor, depth + 1, path + [neighbor]))  

    return min_depth, min_path

def main():
    root, graph = read_graph("input.txt")
    min_depth, min_path = find_min_depth(root, graph)
    
    with open("output.txt", "w") as f:
        f.write(f"Min depth: {min_depth}\n")
        f.write(f"path to min depth: {min_path}")


main()
