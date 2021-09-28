from __future__ import annotations

import math
from pprint import pprint as pp
from typing import Optional


def floyd_warshall(
    graph: dict[str, dict[str, float]]
) -> dict[str, dict[str, float]] | None:
    """Floyd-Warshall algorithm

    O(n^3) time, O(n^2) space

    Based on Tim Roughgarden's lectures

    :returns: shortest distances from each vertex to all the graph's vertices
    or None for negative cycle
    """
    vertices = get_vertices(graph)
    # A[i][j] on the kth iteration is the shortest distance between i and j
    # using only nodes up to k
    A: dict[str, dict[str, float]] = {
        i: {j: math.inf for j in vertices} for i in vertices
    }
    for i in graph:
        A[i].update(graph[i])
    for i in vertices:
        A[i][i] = 0

    for k in vertices:
        for i in vertices:
            for j in vertices:
                # in-place is okay because reusing k would mean a (neg) cycle
                A[i][j] = min(A[i][k] + A[k][j], A[i][j])
    if any(A[i][i] < 0 for i in graph):
        return None

    return A


def get_vertices(graph: dict[str, dict[str, float]]) -> set[str]:
    return set(graph.keys()) | {j for i in graph for j in graph[i]}


def test_tim():
    from .bellman_ford import bellman_ford

    graph = {
        's': {'v': 2, 'x': 4},
        'v': {'w': 2, 'x': 1},
        'w': {'t': 2},
        'x': {'t': 4},
        't': {},
    }
    dist = floyd_warshall(graph)
    want = {v: bellman_ford(graph, v) for v in get_vertices(graph)}
    assert dist == want


def test_tim_sloppy_graph():
    from .bellman_ford import bellman_ford

    graph = {
        's': {'v': 2, 'x': 4},
        'v': {'w': 2, 'x': 1},
        'w': {'t': 2},
        'x': {'t': 4},
    }
    dist = floyd_warshall(graph)
    want = {v: bellman_ford(graph, v) for v in get_vertices(graph)}
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
    from .bellman_ford import bellman_ford

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
    want = {v: bellman_ford(graph, v) for v in get_vertices(graph)}
    assert dist == want


if __name__ == '__main__':
    from .bellman_ford import bellman_ford

    graph: dict[str, dict[str, float]] = {
        's': {'v': 2, 'x': 4},
        'v': {'w': 2, 'x': 1},
        'w': {'t': 2},
        'x': {'t': 4},
    }
    dist = floyd_warshall(graph)
    print('dist:')
    pp(dist)
    want = {v: bellman_ford(graph, v) for v in get_vertices(graph)}
    assert dist == want
