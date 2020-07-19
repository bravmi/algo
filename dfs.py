def dfs(graph: dict, source) -> dict:
    """Depth First Search"""

    explored = set()

    def _dfs(s):
        explored.add(s)
        if s not in graph:  # dead end
            return
        for v in graph[s]:
            if v not in explored:
                _dfs(v)

    _dfs(source)

    return explored


def tests():
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
