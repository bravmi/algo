from heapq import heappop, heappush

INF = float('inf')


def dijkstra(graph: dict, source) -> dict:
    """Dijkstra's shortest path algorithm

    O(m log(m)) time, O(m) space
    log(m) here since it's a heap of edges for simplicity
    (would need to delete-insert a vertex)
    given weak connection assumption

    Based on Tim Roughgarden's lectures
    """

    dist = {}  # type: ignore
    queue = [(0, source)]
    while queue:
        score, v = heappop(queue)
        if v in dist:
            continue
        dist[v] = score
        if v not in graph:  # dead end
            continue
        for w in graph[v]:
            if w not in dist:
                heappush(queue, (dist[v] + graph[v][w], w))
    dist.update({v: INF for v in graph if v not in dist})

    return dist


def test():
    graph = {
        's': {'v': 1, 'w': 4},
        'v': {'w': 2, 't': 6},
        'w': {'t': 3},
    }
    dist = dijkstra(graph, 's')
    assert dist.get('t') == 6


if __name__ == '__main__':
    graph = {
        's': {'v': 1, 'w': 4},
        'v': {'w': 2, 't': 6},
        'w': {'t': 3},
    }
    dist = dijkstra(graph, 's')
    print(f'dist = {dist}')
    assert dist.get('t') == 6
