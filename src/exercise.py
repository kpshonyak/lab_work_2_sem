class DisjointSet:
    def __init__(self, size):
        self.parent = [i for i in range(size)]

    def find(self, u):
        if self.parent[u] != u:
            self.parent[u] = self.find(self.parent[u])
        return self.parent[u]

    def union(self, u, v):
        root_u = self.find(u)
        root_v = self.find(v)
        if root_u != root_v:
            self.parent[root_v] = root_u


def read_matrix(filename):
    matrix = []
    with open(filename, "r") as file:
        for line in file:
            row = line.strip().split(",")
            filtered_row = [int(x) for x in row if x.strip() != ""]
            if filtered_row:
                matrix.append(filtered_row)
    return matrix


def merge_sort(edges):
    if len(edges) <= 1:
        return edges
    mid = len(edges) // 2
    left = merge_sort(edges[:mid])
    right = merge_sort(edges[mid:])
    return merge(left, right)


def merge(left, right):
    result = []
    i, j = 0, 0
    while i < len(left) and j < len(right):
        if left[i][0] <= right[j][0]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    result.extend(left[i:])
    result.extend(right[j:])
    return result


def minimum_cable_length(matrix):
    n = len(matrix)
    edges = []
    for i in range(n):
        for j in range(i + 1, n):
            if matrix[i][j] > 0:
                edges.append((matrix[i][j], i, j))
    sorted_edges = merge_sort(edges)
    ds = DisjointSet(n)
    total = 0
    mst_edges = []
    for weight, u, v in sorted_edges:
        if ds.find(u) != ds.find(v):
            ds.union(u, v)
            total += weight
            mst_edges.append((u, v)) 
    return total, mst_edges


def print_full_graph(matrix):
    print("Повний граф :")
    n = len(matrix)
    for i in range(n):
        for j in range(i + 1, n):
            if matrix[i][j] != 0:
                print(f"{i} -- {j}")


def build_adjacency_list(mst_edges, n):
    adj = [[] for _ in range(n)]
    for u, v in mst_edges:
        adj[u].append(v)
        adj[v].append(u)
    for neighbors in adj:
        neighbors.sort()
    return adj

def print_tree(adj, node, parent=-1, prefix="", is_last=True):
    connector = "\\-- " if is_last else "/-- "
    print(prefix + connector + str(node))

    children = [child for child in adj[node] if child != parent]
    for i, child in enumerate(children):
        last = i == (len(children) - 1)
        new_prefix = prefix + ("    " if is_last else "|   ")
        print_tree(adj, child, node, new_prefix, last)



def print_mst(mst_edges, total_weight, n):
    print("\nМінімальне остовне дерево:")
    adj = build_adjacency_list(mst_edges, n)
    print_tree(adj, 0)
    print("Загальна довжина кабелів:", total_weight)



matrix = read_matrix("islands.csv")
print_full_graph(matrix)
total, mst_edges = minimum_cable_length(matrix)
print_mst(mst_edges, total, len(matrix))
