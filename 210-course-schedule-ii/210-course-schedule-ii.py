class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        ad={i:[] for i in range(numCourses)}
        ordering=collections.deque()
        cycle=set()
        visit=set()
        for course,pre in prerequisites:
            ad[pre].append(course)
        def dfs(crs):
            if crs in cycle:
                return False
            if crs in visit:
                return True

            cycle.add(crs)
            for pre in ad[crs]:
                if dfs(pre) == False:
                    return False
            cycle.remove(crs)
            visit.add(crs)
            ordering.appendleft(crs)
            return True

        for c in range(numCourses):
            if dfs(c) == False:
                return []
        return ordering