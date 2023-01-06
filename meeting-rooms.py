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
    @return: if a person could attend all meetings
    """
    def can_attend_meetings(self, intervals: List[Interval]) -> bool:
        # Write your code here
        intervals.sort(key=lambda i: i.start)
        min_heap=[]
        for i in intervals:
            while min_heap and min_heap[0] < i.start:
                heapq.heappop(min_heap)
            heapq.heappush(min_heap, i.end)
        return len(min_heap) < 2
