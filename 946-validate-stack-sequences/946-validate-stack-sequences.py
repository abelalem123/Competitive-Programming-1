class Solution:
    def validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:
        pu=0
        po=0
        st=[]
        while po<len(popped) and pu<len(popped):
            if st and st[-1]==popped[po]:
                st.pop()
                po+=1
            else:
                st.append(pushed[pu])
                pu+=1
        while pu<len(pushed):
            #print('here push')
            st.push()
            pu+=1
        while po<len(popped):
            #print(st,popped)
            if st and st[-1]==popped[po]:
                st.pop()
                po+=1
            else:
                return False

        return pu==len(pushed) and po==len(popped)
                
                