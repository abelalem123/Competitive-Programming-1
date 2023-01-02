class Solution:
    def validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:
        pu=0
        po=0
        st=[]
        while po<len(popped) and pu<len(pushed):
            if st and st[-1]==popped[po]:
                st.pop()
                po+=1
            else:
                st.append(pushed[pu])
                pu+=1
        while po<len(popped):
            if st and st[-1]==popped[po]:
                st.pop()
                po+=1
            else:
                return False


        return po==len(popped) and pu==len(pushed)
                
                