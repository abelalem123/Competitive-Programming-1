class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack=[]
        result=[0]*len(temperatures)
        for i,n in enumerate(temperatures):
            while stack and n>temperatures[stack[-1]]:
                temp=stack.pop()
                result[temp]=i-temp
            stack.append(i)
        return result