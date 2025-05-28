def check_gas_supply(cities, storages, pipelines):
    graph = {}
    for u, v in pipelines:
        if u not in graph:
            graph[u] = []
        graph[u].append(v)
    result = []

    for storage in storages:
        reachable = []
        visited = []
        queue = [storage]

        while queue:
            current = queue.pop(0)
            if current in visited:
                continue
            visited.append(current)
            reachable.append(current)
            if current in graph:
                for neighbor in graph[current]:
                    if neighbor not in visited:
                        queue.append(neighbor)

        unreachable_cities = []
        for city in cities:
            if city not in reachable:
                unreachable_cities.append(city)

        if unreachable_cities:
            result.append([storage, unreachable_cities])
    return result

def read_input(filename):
    with open(filename, 'r', encoding='utf-8') as f:
        lines = f.readlines()

    cities = lines[0].strip().split(',')
    storages = lines[1].strip().split(',')
    pipelines = [line.strip().split(',') for line in lines[2:]]

    return cities, storages, pipelines

cities, storages, pipelines = read_input('input.txt')
result = check_gas_supply(cities, storages, pipelines)
print(result)
