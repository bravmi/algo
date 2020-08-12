import math
from typing import Optional


def bellman_ford(graph: dict, source) -> Optional[dict]:
    """Bellman-Ford algorithm

    O(n m) time, O(n^2) space (with a sliding row space would be O(m))

    Based on Tim Roughgarden's lectures

    :returns: shortest distances from the source to all the graph's vertices
    or None for negative cycle
    """
    n = len(graph)
    vertices = set(graph.keys()) | {w for v in graph for w in graph[v]}
    # A[i] is dist from the source with a budget of i edges
    A = [{v: math.inf for v in vertices} for _ in range(n + 1)]
    A[0][source] = 0

    for i in range(1, n + 1):
        A[i] = A[i - 1].copy()
        for w in graph:
            for v in graph[w]:
                A[i][v] = min(A[i - 1][w] + graph[w][v], A[i][v])
    if A[n] != A[n - 1]:
        return None

    return A[n - 1]


def test_tim():
    graph = {
        's': {'v': 2, 'x': 4},
        'v': {'w': 2, 'x': 1},
        'w': {'t': 2},
        'x': {'t': 4},
        't': {},
    }
    dist = bellman_ford(graph, 's')
    assert dist == {'s': 0, 'v': 2, 'w': 4, 'x': 3, 't': 6}


def test_tim_negative_cycle():
    graph = {
        's': {'v': 0},
        'v': {'x': -4},
        'w': {'v': 4},
        'x': {'t': 3},
        't': {'w': -5},
    }
    dist = bellman_ford(graph, 's')
    assert dist is None


def test_dasgupta():
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
    dist = bellman_ford(graph, 's')
    want = {'s': 0, 'a': 5, 'b': 5, 'c': 6, 'd': 9, 'e': 7, 'f': 9, 'g': 8}
    assert dist == want


if __name__ == '__main__':
    from pprint import pprint as pp

    graph = {
        's': {'v': 2, 'x': 4},
        'v': {'w': 2, 'x': 1},
        'w': {'t': 2},
        'x': {'t': 4},
        't': {},
    }
    dist = bellman_ford(graph, 's')
    print('dist:')
    pp(dist)
    assert dist is not None
    assert dist['t'] == 6
