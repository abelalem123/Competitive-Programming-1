class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        max_area=0
        visited=set()
        row=len(grid)
        col=len(grid[0])
        def search(r,c):
            area=0
            q=collections.deque()
            visited.add((r,c))
            q.append((r,c))
            while q:
                r,c=q.pop()
                directions=[[1,0],[-1,0],[0,1],[0,-1]]
                for y,x in directions:
                    if ((r+y) in range(row) and 
                        (c+x) in range(col) and
                        grid[r+y][c+x]==1 and
                        (r+y,c+x) not in visited):
                        area+=1
                        visited.add((r+y,c+x))
                        q.append((r+y,c+x))
            return area+1
        for r in range(row):
            for c in range(col):
                if grid[r][c]==1 and (r,c) not in visited:
                    max_area=max(max_area,search(r,c))
        return max_area