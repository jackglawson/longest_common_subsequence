import sys
sys.setrecursionlimit(3000)


def load_strings():
    file = open('strings.txt', 'r')
    x = file.readline().rstrip()
    y = file.readline().rstrip()
    file.close()
    return x, y


x, y = load_strings()
n = len(x)
m = len(y)
# -1 in the cache indicates that the value has not been calculated yet
cache = [[-1 for _ in range(m + 1)] for _ in range(n + 1)]


def lcs(i, j) -> int:
    """We define lcs(i, j) as the lowest common subsequence of x_i and y_j,
    where x_i contains the first i elements of the string x, and similar for y_j"""
    if cache[i][j] != -1:
        result = cache[i][j]

    else:
        # one of the two strings is empty
        if i == 0 or j == 0:
            result = 0

        # they have the same last element, so this can be removed
        elif x[i - 1] == y[j - 1]:
            result = lcs(i - 1, j - 1) + 1

        # they have different last elements
        else:
            result = max(lcs(i - 1, j), lcs(i, j - 1))

        cache[i][j] = result

    return result


def solve():
    return lcs(n, m)


print(solve())
