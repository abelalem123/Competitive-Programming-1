class Solution:
      def minPathCost(self, grid: List[List[int]], moveCost: List[List[int]]) -> int:
        row = len(grid)
        col = len(grid[0])
        # dp[i][j] := min cost to reach grid[i][j]
        dp = [[math.inf for _ in range(col)] for _ in range(row)]
        # for i in range(col):
        #     dp[0][i]=grid[0][i]
        dp[0][:]=grid[0][:]
        for i in range(1, row):
            for j in range(col):
                for k in range(col):
                    dp[i][j] = min(dp[i][j], dp[i - 1][k] +
                             moveCost[grid[i - 1][k]][j] + grid[i][j])

        return min(dp[-1])