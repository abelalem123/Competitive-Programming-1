class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(s)<len(t):
            return ""
        win={}
        
        #character frequency counter for string t
        tfreq={}
        for ch in t:
            tfreq[ch]=tfreq.get(ch,0)+1
        t_size=len(tfreq)
        #track current min window
        min_left=0 
        min_right=math.inf
        
        #variable to inc or decrease so as to compare window size with t_size
        win_formed=0 
        
        #left pointer
        l=0
        for r,char in enumerate(s):
            win[char]=1+win.get(char,0)
            
            #update win_formed if for this current char it has reached the same frequency at tfreq
            if char in t and win[char]==tfreq[char]:
                win_formed+=1
            
            # if current window is equal to t window, 
            # try to decrease it so as to get the minimum win 
            while l<=r and win_formed==t_size:
                left_char=s[l]
                win[left_char]-=1
                
                # decrement win_formed variable if by decreasing the freq at left_char
                #you have decreased it below its counterpart in freqt
                if left_char in t and win[left_char]<tfreq[left_char]:
                    win_formed-=1
                
                #update min window variables if they are smaller than what is stored upto now
                if r-l+1<min_right-min_left+1:
                    min_right=r
                    min_left=l
                l+=1
        return s[min_left:min_right+1] if min_right!=math.inf else ''