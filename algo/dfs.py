from pprint import pprint


def dfs(graph: dict[str, list[str]], source: str) -> set[str]:
    """Depth First Search

    O(m) time, O(n) space
    """
    explored: set[str] = set()

    def dfs_(v: str) -> None:
        if v in explored:
            return
        explored.add(v)

        if v not in graph:  # dead end
            return
        for w in graph[v]:
            dfs_(w)

    dfs_(source)
    return explored


def test_tim():
    graph = {
        's': ['a', 'b'],
        'a': ['s', 'c'],
        'b': ['s', 'c', 'd'],
        'c': ['a', 'b', 'd', 'e'],
        'd': ['b', 'e'],
        'e': ['c', 'd'],
    }
    explored = dfs(graph, 's')
    assert explored == {'s', 'a', 'b', 'c', 'd', 'e'}


def test_dasgupta():
    graph = {
        'a': ['b', 'd'],
        'b': ['a', 'e', 'f'],
        'c': ['a', 'f'],
        'd': ['a', 'g', 'h'],
        'e': ['b', 'i', 'j'],
        'f': ['b', 'c'],
        'g': ['d', 'h'],
        'h': ['d', 'g'],
        'i': ['e', 'j'],
        'j': ['e', 'i'],
        'k': ['l'],
        'l': ['k'],
    }
    explored = dfs(graph, 'a')
    assert explored == {'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j'}


if __name__ == '__main__':
    graph = {
        's': ['a', 'b'],
        'a': ['s', 'c'],
        'b': ['s', 'c', 'd'],
        'c': ['a', 'b', 'd', 'e'],
        'd': ['b', 'e'],
        'e': ['c', 'd'],
    }
    explored = dfs(graph, 's')
    print('explored:')
    pprint(explored)
    assert explored == {'s', 'a', 'b', 'c', 'd', 'e'}
