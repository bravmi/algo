def toposort(graph: dict[str, list[str]]) -> list[str]:
    """Topological sort

    O(m + n) time, O(n) space

    :returns: a list of nodes in topological order
    """
    order: list[str] = []
    explored: set[str] = set()

    def dfs(s: str, hist: set[str]) -> bool:
        explored.add(s)
        hist |= {s}
        for v in graph.get(s, []):
            if v in hist:
                return False
            if v not in explored:
                if not dfs(v, hist.copy()):
                    return False
        order.append(s)
        return True

    for v in graph:
        if v not in explored:
            if not dfs(v, set()):
                return []
    return order[::-1]


def is_valid_order(graph: dict[str, list[str]], order: list[str]) -> bool:
    if not order:
        return False
    for i, v in enumerate(order):
        for w in graph.get(v, []):
            if w in order[:i]:
                return False
    return True


def test_tim():
    graph = {'s': ['v', 'w'], 'v': ['t'], 'w': ['t']}
    order = toposort(graph)
    assert is_valid_order(graph, order)


def test_cycle():
    graph = {'s': ['v', 'w'], 'v': ['t'], 'w': ['t'], 't': ['s']}
    assert not toposort(graph)


def test_min_cycle():
    graph = {'s': ['s']}
    assert not toposort(graph)


if __name__ == '__main__':
    test_cycle()
