class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        #map tempratures to its index
        index=[]
        stack=[]
        result=[0]*len(temperatures)
        for i,n in enumerate(temperatures):
            while stack and n>stack[-1]:
                temp=stack.pop()
                idx=index.pop()
                result[idx]=i-idx
            stack.append(n)
            index.append(i)
        return result