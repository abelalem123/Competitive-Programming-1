class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        row=len(obstacleGrid)
        col=len(obstacleGrid[0])
        dp=[[0 for _ in range(col)] for _ in range(row)]
        if obstacleGrid[0][0]==0:
            dp[0][0]=1
        for i in range(1,row):
            if obstacleGrid[i][0]==0:
                dp[i][0]=dp[i-1][0]
        for j in range(1,col):
            if obstacleGrid[0][j]==0:
                dp[0][j]=dp[0][j-1]
        for r in range(1,row):
            for c in range(1,col):
                if obstacleGrid[r][c]==0:
                    dp[r][c]=dp[r-1][c]+dp[r][c-1]
        return dp[-1][-1]
            