class Solution:
    def average(self, salary: List[int]) -> float:
        
        min_=math.inf
        max_=-math.inf
        result=0
        for i in salary:
            min_=min(min_,i)
            max_=max(max_,i)
            result+=i
        return (result - min_ - max_)/(len(salary) - 2)
                