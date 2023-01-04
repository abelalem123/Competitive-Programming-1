class Solution:
    def average(self, salary: List[int]) -> float:
        
        min_=min(salary)
        max_=max(salary)
        result=0
        for i in salary:
            if i==min_ or i==max_:
                continue
            result+=i
        return result/(len(salary)-2)
                