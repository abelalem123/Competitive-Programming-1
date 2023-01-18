class Solution:
    def minDeletionSize(self, strs: List[str]) -> int:
        """
        abc
        bce
        check every row for every column
        """
        remove=0
        
        for col in range(len(strs[0])):
            is_sorted=True
            first=strs[0][col]
            for row in range(1,len(strs)):
                is_sorted = is_sorted and first <= strs[row][col]
                first=strs[row][col]
            if not is_sorted:
                remove+=1
        return remove