import copy
from pprint import pprint as pp
from typing import Optional

from bellman_ford import bellman_ford
from dijkstra import dijkstra


def johnson(graph: dict) -> Optional[dict]:
    """Johnson's algorithm

    O(n m log(m)) time, O(n^2) space

    Based on Tim Roughgarden's lectures

    :returns: shortest distances from each vertex to all the graph's vertices
    or None for negative cycle
    """
    vertices = set(graph.keys()) | {w for v in graph for w in graph[v]}
    graph_prime = copy.deepcopy(graph)
    assert None not in graph
    s = None
    graph_prime[s] = {v: 0 for v in vertices}

    weight = bellman_ford(graph_prime, s)
    if weight is None:
        return None
    for v in graph_prime:
        for w in graph_prime[v]:
            graph_prime[v][w] += weight[v] - weight[w]

    dist = {v: dijkstra(graph_prime, v) for v in vertices}
    for v in vertices:
        dist[v].pop(s, None)  # my dijkstra will return inf for s
        for w in vertices:
            dist[v][w] -= weight[v] - weight[w]
    return dist


def test_tim():
    from floyd_warshall import floyd_warshall

    graph = {
        's': {'v': 2, 'x': 4},
        'v': {'w': 2, 'x': 1},
        'w': {'t': 2},
        'x': {'t': 4},
        't': {},
    }
    dist = johnson(graph)
    want = floyd_warshall(graph)
    assert dist == want


def test_tim_sloppy_graph():
    from floyd_warshall import floyd_warshall

    graph = {
        's': {'v': 2, 'x': 4},
        'v': {'w': 2, 'x': 1},
        'w': {'t': 2},
        'x': {'t': 4},
    }
    dist = johnson(graph)
    want = floyd_warshall(graph)
    assert dist == want


def test_tim_negative_cycle():
    graph = {
        's': {'v': 0},
        'v': {'x': -4},
        'w': {'v': 4},
        'x': {'t': 3},
        't': {'w': -5},
    }
    dist = johnson(graph)
    assert dist is None


def test_dasgupta():
    from floyd_warshall import floyd_warshall

    graph = {
        's': {'a': 10, 'g': 8},
        'a': {'e': 2},
        'b': {'a': 1, 'c': 1},
        'c': {'d': 3},
        'd': {'e': -1},
        'e': {'b': -2},
        'f': {'a': -4, 'e': -1},
        'g': {'f': 1},
    }
    dist = johnson(graph)
    want = floyd_warshall(graph)
    assert dist == want


if __name__ == '__main__':
    from floyd_warshall import floyd_warshall

    graph = {
        's': {'v': 2, 'x': 4},
        'v': {'w': 2, 'x': 1},
        'w': {'t': 2},
        'x': {'t': 4},
    }
    dist = johnson(graph)
    print('dist:')
    pp(dist)
    want = floyd_warshall(graph)
    assert dist == want
