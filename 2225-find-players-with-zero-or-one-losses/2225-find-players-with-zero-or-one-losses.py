class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        result=defaultdict(int)
        wins =set()
        
        #print(result)
        for w,l in matches:
            result[l]+=1
            wins.add(w)
        zero=[]
        one=[]
        for k,v in result.items():
            print(k in wins)
            if v==1:
                one.append(k)
        for w in wins:
            if w not in result:
                zero.append(w)
        return [sorted(zero),sorted(one)]
    