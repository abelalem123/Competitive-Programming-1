class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        pair=[(po,sp) for po,sp in zip(position,speed)]
        stack=[]
        pair.sort(reverse=True)
        for pos,speed in pair:
            time_to_target= (target-pos)/speed
            stack.append(time_to_target)
            if len(stack)>=2:
                # E.g using the stack
                #   10(pos)   6(pos)
                #   _---_     _---_ 
                #  stack[-2]  stack[-1]
                #  ahead        curr
                # current car arrival time <= to ahead of it means
                # current car will arrive before ahead of it but it can't since it is one lane
                #thus its speed will be limited by ahead will arrive in time similar to that of ahead
                # thus we pop it from the stack
                curr=stack[-1] 
                ahead=stack[-2] 
                
                if curr<= ahead: #meaning that the car at pos 6 will reach target 
                    #before the one at pos10
                    #pop it because it will have the speed of the slower one (car at pos 10)
                    stack.pop() 
        return len(stack)
                