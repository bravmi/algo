def dfs(graph: dict, source) -> set:
    """Depth First Search"""
    explored: set = set()

    def _dfs(v) -> None:
        if v in explored:
            return
        explored.add(v)

        if v not in graph:  # dead end
            return
        for w in graph[v]:
            _dfs(w)

    _dfs(source)
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
    print(f'explored = {explored}')
    assert explored == {'s', 'a', 'b', 'c', 'd', 'e'}
