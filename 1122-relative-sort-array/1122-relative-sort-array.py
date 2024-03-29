
        
class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        pos={n:i for i,n in enumerate(arr2)}
        offset = len(arr2)
        return sorted(arr1,key=lambda a:pos.get(a,offset+a))
        
        # #print(pos)
        # def compare(item1, item2):
        #     if pos[item1] < pos[item2]:
        #         return -1
        #     elif pos[item1] > pos[item2]:
        #         return 1
        #     else:
        #         return 0
        
