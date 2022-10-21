class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        rowset=set()
        colset=set()
        num=2**31 + 1
        row=len(matrix)
        col=len(matrix[0])
        row0=False
        col0=False
        for i in range(row):
            if matrix[i][0]==0:
                col0=True
                break
        for j in range(col):
            if matrix[0][j]==0:
                row0=True
                break
        for i in range(1,row):
            for j in range(1,col):
                if matrix[i][j]==0:
                    matrix[i][0]=0
                    matrix[0][j]=0

        for i in range(1,row):
            for j in range(1,col):
                if matrix[i][0]==0 or matrix[0][j]==0:
                    matrix[i][j]=0
        if col0:
            for i in range(row):
                matrix[i][0]=0
        if row0:
            for j in range(col):
                matrix[0][j]=0
            