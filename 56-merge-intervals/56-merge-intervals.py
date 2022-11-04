class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=lambda i:i[0])
        res=[]
        init=intervals[0].copy()
        for i in range(1,len(intervals)):
            if init[1]<intervals[i][0]:
                res.append(init.copy())
                init[0]=intervals[i][0]
                init[1]=intervals[i][1]
            if init[1]>=intervals[i][0]:
                #init[0]=min(init[0],intervals[i][0])
                init[1]=max(init[1],intervals[i][1])
        res.append(init)
        return res
                
                