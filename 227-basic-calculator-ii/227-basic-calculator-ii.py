class Solution:
    def calculate(self, s: str) -> int:
        stack=[]
        current_num=0
        op='+'
        for i,c in enumerate(s):
            if c.isdigit():
                current_num=(current_num*10)+int(c)

            if (not c.isdigit() and c!=' ') or i==len(s)-1:
                if op=='+':
                    stack.append(current_num)
                elif op=='-':
                    stack.append(-current_num)
                elif op=='*':
                    stack.append(stack.pop()*current_num)
                elif op=='/':
                    stack.append(int(stack.pop()/current_num))
                op=c
                current_num=0
        result=0
        while stack:
            result+=stack.pop()
        return result