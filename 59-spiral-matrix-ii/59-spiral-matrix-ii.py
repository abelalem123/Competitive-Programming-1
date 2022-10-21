class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        res=[[0 for i in range(n)] for _ in range(n)]
        n=len(res)
        left,right=0,n-1
        top,bottom=0,n-1
        cycle=0
        count=1
        
        while (left<=right and top<=bottom):
            if cycle==0:
                for i in range(left,right+1):
                    res[top][i]=count
                    count+=1
                top+=1
                cycle=1
            elif cycle==1:
                for i in range(top,bottom+1):
                    res[i][right]=count
                    count+=1
                right-=1
                cycle=2
            elif cycle==2:
                for i in range(right,left-1,-1):
                    res[bottom][i]=count
                    count+=1
                bottom-=1
                cycle=3
            elif cycle==3:
                for i in range(bottom,top-1,-1):
                    res[i][left]=count
                    count+=1
                left+=1
                cycle=0
        return res