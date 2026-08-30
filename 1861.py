from typing import List

class Solution:
    def rotate(self, grid: List[List[str]]) -> List[List[str]]:
        m, n = len(grid), len(grid[0])
        result = [['.'] * m for _ in range(n)]
        for r in range(m):
            k = n  - 1
            for c in range(n - 1, -1, -1):
                if grid[r][c] == '*':
                    result[c][m - r - 1] = '*'
                    k = c - 1
                if grid[r][c] == '#':
                    result[k][m - r - 1] = '#'
                    k -= 1
        return result