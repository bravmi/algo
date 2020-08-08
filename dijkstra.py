import math
from heapq import heappop, heappush


def dijkstra(graph: dict, source) -> dict:
    """Dijkstra's shortest path algorithm

    O(m log(m)) time, O(m) space
    log(m) here since it's a heap of edges for simplicity
    (would need to delete-insert a vertex for a heap of vertices)

    Based on Tim Roughgarden's lectures

    :returns: distances from the source to the graph's vertices
    """
    dist: dict = {}

    queue = [(0, source)]
    while queue:
        score, v = heappop(queue)
        if v in dist:
            continue
        dist[v] = score
        if v not in graph:  # dead end
            continue

        for w in graph[v]:
            if w not in dist:  # optimization
                heappush(queue, (dist[v] + graph[v][w], w))

    vertices = set(graph.keys()) | {w for v in graph for w in graph[v]}
    dist.update({v: math.inf for v in vertices if v not in dist})
    return dist


def test4():
    graph = {
        's': {'v': 1, 'w': 4},
        'v': {'w': 2, 't': 6},
        'w': {'t': 3},
        't': {},
    }
    dist = dijkstra(graph, 's')
    assert dist['t'] == 6


if __name__ == '__main__':
    graph = {
        's': {'v': 1, 'w': 4},
        'v': {'w': 2, 't': 6},
        'w': {'t': 3},
    }
    dist = dijkstra(graph, 's')
    print(f'dist = {dist}')
    assert dist['t'] == 6
