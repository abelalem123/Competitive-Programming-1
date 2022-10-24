class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        m=len(matrix)
        n=len(matrix[0])
        dp=[[0 for _ in range(n)]for _ in range(m)]
        max_area=dp[0][0]
        for r in range(m):
            if matrix[r][0]=='1':
                dp[r][0]=1
                max_area=max(max_area,dp[r][0])
        for c in range(n):
            if matrix[0][c]=='1':
                dp[0][c]=1
                max_area=max(max_area,dp[0][c])
        for r in range(1,m):
            for c in range(1,n):
                x=dp[r-1][c]
                y=dp[r][c-1]
                z=dp[r-1][c-1]
                val=int(matrix[r][c])
                if x and y and z and val:
                    dp[r][c]=min(x,y,z)+1
                    
                elif val:
                    dp[r][c]=1
                max_area=max(max_area,dp[r][c])

        return max_area**2