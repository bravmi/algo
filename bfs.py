import collections as co
import math


def bfs(graph: dict, source) -> dict:
    """Breadth First Search

    :returns: distances from the source to all the graph's vertices
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

    vertices = set(graph.keys()) | {w for v in graph for w in graph[v]}
    dist.update({v: math.inf for v in vertices if v not in dist})
    return dist


def test_tim():
    graph = {
        's': ['a', 'b'],
        'a': ['s', 'c'],
        'b': ['s', 'c', 'd'],
        'c': ['a', 'b', 'd', 'e'],
        'd': ['b', 'e'],
        'e': ['c', 'd'],
    }
    dist = bfs(graph, 's')
    assert dist == {'s': 0, 'a': 1, 'b': 1, 'c': 2, 'd': 2, 'e': 3}


def test_tim_directed():
    graph = {
        's': ['v', 'w'],
        'v': ['w', 't'],
        'w': ['t'],
    }
    dist = bfs(graph, 's')
    assert dist == {'s': 0, 'v': 1, 'w': 1, 't': 2}


def test_dasgupta():
    graph = {
        'a': ['b', 'c'],
        'b': ['c', 'd', 'e'],
        'c': ['b', 'd', 'e'],
        'd': [],
        'e': ['d'],
    }
    dist = bfs(graph, 'a')
    assert dist == {'a': 0, 'b': 1, 'c': 1, 'd': 2, 'e': 2}


if __name__ == '__main__':
    from pprint import pprint as pp

    graph = {
        's': ['a', 'b'],
        'a': ['s', 'c'],
        'b': ['s', 'c', 'd'],
        'c': ['a', 'b', 'd', 'e'],
        'd': ['b', 'e'],
        'e': ['c', 'd'],
    }
    dist = bfs(graph, 's')
    print('dist:')
    pp(dist)
    assert dist['e'] == 3
