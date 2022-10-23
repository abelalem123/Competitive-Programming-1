class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        rows=len(board)
        cols=len(board[0])
        visited=set()
        def dfs(row,col,i)->bool:
            if i==len(word):
                return True
            if (row<0 or col<0 or 
                row>=rows or 
                col>=cols or 
                board[row][col]!=word[i]):
                return False
            board[row][col]=' '
            found=( 
                dfs(row+1,col,i+1) or 
                dfs(row-1,col,i+1) or 
                dfs(row,col+1,i+1) or 
                dfs(row,col-1,i+1) 
                )
            board[row][col]=word[i]
            return found
                
        for row in range(rows):
            for col in range(cols):
                if board[row][col]==word[0]:
                    if dfs(row,col,0):
                        return True
        return False

