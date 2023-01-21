class Solution:
    def searchMatrix(self,matrix, target: int) -> bool:
        """
        1 3 4 5 7 l lm
        10 11 16 20 m h
        23 30 34 60 h
        
        o(log(m*n))
        """
        row=len(matrix)
        col=len(matrix[0])
        low=0
        high=row-1
        mid=0
        rmid=0
        #row o(log(row))
        while(high>=low):
            mid=low+(high-low)//2
            if target<=matrix[mid][-1] and target >=matrix[mid][0]:
                break
            elif target<matrix[mid][-1]: # also smaller than matrix[mid][0]
                high=mid-1
            elif target>matrix[mid][-1]:
                low=mid+1
            else:
                return False
            
        #col o(log(col))
        r=mid #get the appropriate row from the previous bisect
        low=0
        high=col-1
        while(high>=low):
            mid=low+(high-low)//2
            if target==matrix[r][mid]:
                return True
            if target<matrix[r][mid]:
                high=mid-1
            elif target>matrix[r][mid]:
                low=mid+1
            # else:
            #     return True
            
        return False
                