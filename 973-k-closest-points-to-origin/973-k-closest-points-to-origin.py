class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        """[[1,3],[4,2],[2,1]]
        calculate distance of each
        1^2+3^2, 4^2+2^2, 2^2+1^2
        10, 20, 5
        sort the distance -> 5,20,
        iterate untill k and return corresponding
        """
        return sorted(points,key=lambda point: point[0]**2+point[1]**2)[:k]
        
        # distance={}
        # i=0
        # for x,y in points:
        #     distance[i]=x**2+y**2
        #     i+=1
        # distance_sorted=sorted(distance.items(),key=lambda a:a[1])
        # res=[]
        # for i in range(k):
        #      res.append(points[distance_sorted[i][0]])
        # return res