class Solution:
    def isValid(self, s: str) -> bool:
        st=list()
        pair={')':'(', '}':'{', ']':'['}
        for idx,i in enumerate(s):
            if i not in pair:
                st.append(i)
                continue
            st.pop() if st and st[-1]==pair[i] else st.append(i)
        return (not st)
        
                
        