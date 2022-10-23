class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res=[]
        def search(i,curr,total):
            if total>target or i>=len(candidates):
                return
            if total==target:
                res.append(curr.copy())
                return
            #decision to include i into curr(or those that to be added)
            curr.append(candidates[i])
            search(i,curr,total+candidates[i])
            #decision not to include i into curr(or those that to be added)
            curr.pop()
            search(i+1,curr,total)
        search(0,[],0)
        return res