class Solution:
    def __init__(self):
        self.solutions=0
    def solveSudoku(self, board) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        for r in range(9):
            for c in range(9):
                if board[r][c]==".":
                    for i in range(1,10):
                        if self.is_valid(board,r,c,str(i)):
                            board[r][c]=str(i)
                            self.solveSudoku(board)
                            if self.solutions==1:
                                return
                            board[r][c]="."
                    return
        self.solutions=1

    def is_valid(self,board,r,c,n):
        ## check column anc row
        for i in range(9):
            if board[r][i]==n:
                return False
            if board[i][c]==n:
                return False
        r0=(r//3)*3
        c0=(c//3)*3
        for i in range(3):
            for j in range(3):
                if board[r0+i][c0+j]==n:
                    return False
        return True