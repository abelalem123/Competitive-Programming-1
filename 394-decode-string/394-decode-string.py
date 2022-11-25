class Solution:
    def decodeString(self, s: str) -> str:
        char_list=[]
        digits=0
        mult=[]
        for ch in s:
            if ch.isdigit():
                digits=digits*10+int(ch)
            elif ch=='[':
                #we have got the number whose digits we have been forming
                char_list.append(str(digits)) 
                char_list.append(ch)
                digits=0
            elif ch!=']': #characters other than [, ] or digit
                char_list.append(ch)
            else: #]
                temp=[]
                while char_list[-1]!='[':
                    temp.append(char_list.pop())
                    
                char_list.pop() #[ is popped
                multiplier=int(char_list.pop())
            
                for i in range(multiplier):
                    for i in range(len(temp)-1,-1,-1):
                        char_list.append(temp[i])
        return ''.join(char_list)