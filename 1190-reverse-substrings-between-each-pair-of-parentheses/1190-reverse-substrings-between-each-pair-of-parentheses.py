class Solution:
    def reverseParentheses(self, s: str) -> str:
        stack=[]
        for i in s:
            if i!=')':
                stack.append(i)
            elif i==')':
                temp=[]
                x=stack.pop()
                while x!='(':
                    temp.append(x)
                    x=stack.pop()
                stack.extend(temp)
        #print(stack)
        return ''.join(i for i in stack)