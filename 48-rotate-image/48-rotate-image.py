class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        rows=len(matrix)-1
        cols=len(matrix[0])
        def subrotate(row,col,length):
            for i in range(length-1):
                temp=matrix[row][col+i]
                matrix[row][col+i]=matrix[rows-(col+i)][row]
                matrix[rows-(col+i)][row]=matrix[rows-row][rows-(col+i)]
                matrix[rows-row][rows-(col+i)]=matrix[col+i][rows-row]
                matrix[col+i][rows-row]=temp
        i=len(matrix)
        j=0
        while i>=2:
            subrotate(j,j,i)
            j+=1
            i-=2
        
        
        
        