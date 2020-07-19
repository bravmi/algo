def levenshtein(s1: str, s2: str) -> int:
    m = len(s1)
    n = len(s2)

    # D[i][j] holds the distance between the first i characters of s1 and the
    # first j characters of s2
    D = [[0] * (n + 1) for _ in range(m + 1)]
    for i in range(m + 1):
        D[i][0] = i
    for j in range(n + 1):
        D[0][j] = j

    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if s1[i - 1] == s2[j - 1]:
                # free substitution
                D[i][j] = D[i - 1][j - 1]
            else:
                # best of deletion / insertion / substitution correspondingly
                D[i][j] = 1 + min(D[i - 1][j], D[i][j - 1], D[i - 1][j - 1])
    return D[m][n]


def tests():
    assert levenshtein('sitting', 'kitten') == 3
    assert levenshtein('Sunday', 'Saturday') == 3


if __name__ == '__main__':
    pass
