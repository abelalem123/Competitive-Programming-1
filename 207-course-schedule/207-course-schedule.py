class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        ad={}
        visited=set()
        #length of prerequisites
        for i,x in prerequisites:
            if i not in ad:
                ad[i]=list()
                ad[i].append(x)
            if i in ad:
                ad[i].append(x)
            if x not in ad:
                ad[x]=list()  
        def is_cycle(node,track):
            track.add(node)
            visited.add(node)
            for child in ad[node]:
                if child not in visited and is_cycle(child,track):
                    return True
                if child in track:
                    return True
            track.remove(node)
            return False
        for node in ad:
            track=set()
            if node not in visited:
                if is_cycle(node,track):
                    return False
        return True