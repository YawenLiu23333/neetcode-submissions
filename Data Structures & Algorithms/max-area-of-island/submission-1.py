class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        row, col = len(grid), len(grid[0])
        res = 0

        def dfs(r, c):
            nonlocal res
            nonlocal area
            if r < 0 or r >= row or c < 0 or c >= col:
                return 

            if grid[r][c] == 0:
                return
            area += 1
            grid[r][c] = 0

            dfs(r, c + 1)
            dfs(r, c - 1)
            dfs(r + 1, c)
            dfs(r - 1, c)

            res = max(res, area)

        for r in range(row):
            for c in range(col):
                if grid[r][c] == 1:
                    area = 0
                    dfs(r, c)
        return res
