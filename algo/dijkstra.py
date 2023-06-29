import math
from heapq import heappop, heappush
from pprint import pprint as pp


def dijkstra(graph: dict[str, dict[str, float]], source: str) -> dict[str, float]:
    """Dijkstra's shortest path algorithm

    O(m log(m)) time, O(m) space
    log(m) here since it's a heap of edges' heads (as opposed to vertices)
    for simplicity, which is fine because the best one will win anyway.
    For log(n) would need a custom heap of vertices with delete-insert

    Based on Tim Roughgarden's lectures

    :returns: distances from the source to all the graph's vertices
    """
    dist: dict[str, float] = {}

    # second elements must be comparable
    queue: list[tuple[float, str]] = [(0, source)]
    while queue:
        score, v = heappop(queue)
        if v in dist:
            continue
        dist[v] = score
        if v not in graph:  # dead end
            continue

        for w in graph[v]:
            if w in dist:  # optimization
                continue
            score = dist[v] + graph[v][w]
            heappush(queue, (score, w))

    vertices = set(graph.keys()) | {w for v in graph for w in graph[v]}
    dist.update({v: math.inf for v in vertices if v not in dist})
    return dist


def test_tim():
    graph = {
        's': {'v': 1, 'w': 4},
        'v': {'w': 2, 't': 6},
        'w': {'t': 3},
        't': {},
    }
    dist = dijkstra(graph, 's')
    assert dist == {'s': 0, 'v': 1, 'w': 3, 't': 6}


def test_dasgupta():
    graph = {
        'a': {'b': 4, 'c': 2},
        'b': {'c': 3, 'd': 2, 'e': 3},
        'c': {'b': 1, 'd': 4, 'e': 5},
        'd': {},
        'e': {'d': 1},
    }
    dist = dijkstra(graph, 'a')
    assert dist == {'a': 0, 'b': 3, 'c': 2, 'd': 5, 'e': 6}


if __name__ == '__main__':
    graph = {
        's': {'v': 1, 'w': 4},
        'v': {'w': 2, 't': 6},
        'w': {'t': 3},
    }
    dist = dijkstra(graph, 's')  # type: ignore
    print('dist:')
    pp(dist)
    assert dist['t'] == 6
