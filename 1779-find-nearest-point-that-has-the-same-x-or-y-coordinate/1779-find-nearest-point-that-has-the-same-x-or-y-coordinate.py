class Solution:
    def nearestValidPoint(self, x: int, y: int, points: List[List[int]]) -> int:
        
        min_dist=math.inf
        index=-1
        for i,p in enumerate(points):
            x2=p[0]
            y2=p[1]
            if x==x2 or y==y2:
                dist= abs(x-x2) + abs(y-y2)
                if dist < min_dist:
                    index = i
                    min_dist = dist
        return index
                