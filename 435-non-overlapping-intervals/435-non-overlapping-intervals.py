class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda k:k[0]) #sort by start
        min_heap = []
        l_start = intervals[0][0]
        l_end = intervals[0][1]
        count = 0
        for i in range(1,len(intervals)):
            cur_start = intervals[i][0]
            cur_end = intervals[i][1]
            if l_end > cur_start:
                if l_end >= cur_end:
                    l_start = cur_start
                    l_end = cur_end
                count +=1
            else:
                l_start = cur_start
                l_end = cur_end
        return count 
        #[1,3] [1,4]
        # ____
        # __________
        # _______________________
        # 1 2 3 4 5 6 7 8 9 10 11
        return count