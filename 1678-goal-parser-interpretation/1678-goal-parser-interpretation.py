class Solution:
    def interpret(self, command: str) -> str:
        dec=[]
        for i in command:
            if i==')':
                if dec.pop()=='(':
                    dec.append('o')
                else:
                    while dec[-1]!='(':
                        dec.pop()
                    dec.pop()
                    dec.append('al')
            else:
                dec.append(i)
        return ''.join(dec)