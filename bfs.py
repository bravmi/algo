import collections as co
import math


def bfs(graph: dict, source) -> dict:
    """Breadth First Search

    :returns: distances from the source to the graph's vertices
    """

    dist = {source: 0}
    queue = co.deque([source])
    while queue:
        v = queue.popleft()
        if v not in graph:  # dead end
            continue
        for w in graph[v]:
            if w not in dist:
                dist[w] = dist[v] + 1
                queue.append(w)
    dist.update({v: math.inf for v in graph if v not in dist})

    return dist


def test():
    graph = {
        's': ['a', 'b'],
        'a': ['s', 'c'],
        'b': ['s', 'c', 'd'],
        'c': ['a', 'b', 'd', 'e'],
        'd': ['b', 'e'],
        'e': ['c', 'd'],
    }
    dist = bfs(graph, 's')
    assert dist.get('e') == 3


def test_directed():
    graph = {
        's': {'v': 1, 'w': 4},
        'v': {'w': 2, 't': 6},
        'w': {'t': 3},
    }
    dist = bfs(graph, 's')
    assert dist.get('t') == 2


if __name__ == '__main__':
    graph = {
        's': ['a', 'b'],
        'a': ['s', 'c'],
        'b': ['s', 'c', 'd'],
        'c': ['a', 'b', 'd', 'e'],
        'd': ['b', 'e'],
        'e': ['c', 'd'],
    }
    dist = bfs(graph, 's')
    print(f'dist = {dist}')
    assert dist.get('e') == 3
