class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack=[]
        for i in tokens:
            if i.isdigit() or i.lstrip('-').isdigit():
                stack.append(i)
            else:
                operand2=float(stack.pop())
                operand1=float(stack.pop())
                res=eval(f'{operand1} {i} {operand2}')
                stack.append(int(res))
        return stack[0]

    