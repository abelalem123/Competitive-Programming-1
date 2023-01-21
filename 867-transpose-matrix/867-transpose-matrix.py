class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        result=[]
        for col in range(len(matrix[0])):
            temp=[]
            for row in range(len(matrix)):    
                temp.append(matrix[row][col])
            result.append(temp)
        return result