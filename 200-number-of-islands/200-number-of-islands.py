class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        rows=len(grid)
        cols=len(grid[0])
        visited=set()
        islands=0
        def search(r,c):
            q=collections.deque()
            q.append((r,c))
            visited.add((r,c))
            while q:
                r,c=q.popleft()
                directions=[(1,0),(-1,0),(0,1),(0,-1)]
                for dy,dx in directions:
                    if ((r+dy) in range(rows) 
                        and (c+dx) in range(cols)
                        and (r+dy,c+dx) not in visited
                        and grid[r+dy][c+dx]=='1'):
                        q.append((r+dy,c+dx))
                        visited.add((r+dy,c+dx))
        for row in range(rows):
            for col in range(cols):
                if grid[row][col]=='1' and (row,col) not in visited:
                    search(row,col)
                    islands+=1
        return islands
                    
        