class Solution:
    def countPairs(self, deliciousness: List[int]) -> int:
        ub=2**21
        i=1
        two_powers=[]
        while i<=ub:
            two_powers.append(i)
            i*=2
        ans = 0
        freq=defaultdict(int)
        for d in deliciousness:
            for power in two_powers:
                ans += freq[power - d]
            freq[d] += 1
        return ans % (10**9 + 7)

    
        