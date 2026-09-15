from typing import List

def rotate_the_box(grid: List[List[str]]) -> List[List[str]]:
    m, n = len(grid), len(grid[0])
    result = [['.'] * m for _ in range(n)]
    for r in range(m):
        write = n  - 1
        for c in range(n - 1, -1, -1):
            if grid[r][c] == '*':
                result[c][m - r - 1] = '*'
                write = c - 1
            if grid[r][c] == '#':
                result[write][m - r - 1] = '#'
                write -= 1
    return result
