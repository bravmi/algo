import math
from typing import Optional


def floyd_warshall(graph: dict) -> Optional[dict]:
    """Floyd-Warshall algorithm

    O(n^3) time, O(n^2) space

    Based on Tim Roughgarden's lectures

    :returns: shortest distances from each vertex to all the graph's vertices
    or None for negative cycle
    """
    vertices = set(graph.keys()) | {w for v in graph for w in graph[v]}
    # A[i][j] on the kth iteration is the shortest distance between i and j
    # using only nodes up to k
    A = {i: {j: graph[i].get(j, math.inf) for j in vertices} for i in vertices}
    for i in graph:
        A[i][i] = 0

    for k in graph:
        for i in graph:
            for j in graph:
                A[i][j] = min(A[i][k] + A[k][j], A[i][j])
    if any(A[i][i] < 0 for i in graph):
        return None

    return A


def test_tim():
    from bellman_ford import bellman_ford

    graph = {
        's': {'v': 2, 'x': 4},
        'v': {'w': 2, 'x': 1},
        'w': {'t': 2},
        'x': {'t': 4},
        't': {},
    }
    dist = floyd_warshall(graph)
    want = {v: bellman_ford(graph, v) for v in graph}
    assert dist == want


def test_tim_negative_cycle():
    graph = {
        's': {'v': 0},
        'v': {'x': -4},
        'w': {'v': 4},
        'x': {'t': 3},
        't': {'w': -5},
    }
    dist = floyd_warshall(graph)
    assert dist is None


def test_dasgupta():
    from bellman_ford import bellman_ford

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
    dist = floyd_warshall(graph)
    want = {v: bellman_ford(graph, v) for v in graph}
    assert dist == want


if __name__ == '__main__':
    from bellman_ford import bellman_ford
    from pprint import pprint as pp

    graph = {
        's': {'v': 2, 'x': 4},
        'v': {'w': 2, 'x': 1},
        'w': {'t': 2},
        'x': {'t': 4},
        't': {},
    }
    dist = floyd_warshall(graph)
    print('dist:')
    pp(dist)
    want = {v: bellman_ford(graph, v) for v in graph}
    assert dist == want
