class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        m=len(matrix)
        n=len(matrix[0])
        left=0
        right=n-1
        top=0
        bottom=m-1
        cycle=0
        res=[]
        while(left<=right and top<=bottom):
            if cycle==0:
                for i in range(left,right+1):
                    res.append(matrix[top][i])
                top+=1
                cycle=1
            elif cycle==1:
                for i in range(top,bottom+1):
                    res.append(matrix[i][right])    
                right-=1
                cycle=2
            elif cycle==2:
                for i in range(right,left-1,-1):
                    res.append(matrix[bottom][i])
                bottom-=1
                cycle=3
            elif cycle==3:
                for i in range(bottom,top-1,-1):
                    res.append(matrix[i][left])
                left+=1
                cycle=0
        return res
   