class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        stack=[]
        for i in num:
            while k>0 and stack and int(i)<int(stack[-1]):
                stack.pop()
                k-=1
            stack.append(i)
        #incase the number was in increasing order, 
        #we just take the left most digits
        res=''.join(stack[:len(stack)-k]) 
        return str(int(res)) if res else '0'