class NumMatrix:
    #using green outline example
    def __init__(self, matrix: List[List[int]]):
        row=len(matrix)
        col=len(matrix[0])
        self.premat=[[0 for _ in range(col+1)]for _ in range(row+1)]
        for r in range(row):
            row_rectangle=0 
            for c in range(col):
                row_rectangle+=matrix[r][c] # a flat 1d rectangle upto the current 5
                above_rectangle=self.premat[r][c+1] # a square formed just above it 3 0
                self.premat[r+1][c+1]=row_rectangle + above_rectangle

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        row1, col1,row2,col2=row1+1, col1+1,row2+1,col2+1   # for offsets
        row_rectangle=self.premat[row1-1][col2] #rectangle above it e.g 3 0 1 4
        col_rectangle=self.premat[row2][col1-1] # rectangle to left e.g 3 5 1 4 tower
        top_left_rectangle=self.premat[row1-1][col1-1] # cause we are minusing 3 two times
        biggest_rectangle=self.premat[row2][col2]
        return biggest_rectangle + top_left_rectangle - row_rectangle - col_rectangle 
# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)