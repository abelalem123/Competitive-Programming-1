#if current starts before prev ends push, else pop first then push
from typing import (
    List,
)
from lintcode import (
    Interval,
)
import heapq
"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    """
    @param intervals: an array of meeting time intervals
    @return: the minimum number of conference rooms required
    """
    def minMeetingRooms(self, intervals):
        if not intervals:
            return 0
        intervals.sort(key=lambda interval: interval.start)
        min_heap = [] # stores only end_time
        
        for i in intervals:
            if not min_heap:
                heapq.heappush(min_heap,i.end)
                continue
            if i.start < min_heap[0]: # starts before prev ends
                heapq.heappush(min_heap, i.end)
            else:
                heapq.heappushpop(min_heap, i.end)
        return len(min_heap)
