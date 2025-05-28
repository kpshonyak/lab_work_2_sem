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
    file = open(filename, "r")
    for line in file:
        row = line.strip().split(",")
        filtered_row = [int(x) for x in row if x.strip() != ""]
        if filtered_row:  
            matrix.append(filtered_row)
    file.close()
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
    i = 0
    j = 0

    while i < len(left) and j < len(right):
        if left[i][0] <= right[j][0]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    while i < len(left):
        result.append(left[i])
        i += 1

    while j < len(right):
        result.append(right[j])
        j += 1

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
    for weight, u, v in sorted_edges:
        if ds.find(u) != ds.find(v):
            ds.union(u, v)
            total += weight

    return total


matrix = read_matrix("islands.csv")
result = minimum_cable_length(matrix)
print("Мінімальна довжина кабелю:", result)
