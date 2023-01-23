class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        all_words = Counter(words)
        
        word=''.join(words)
        
        word_dict={}
        for i in word:
            if i in word_dict:
                word_dict[i]+=1
            else:
                word_dict[i]=1
        
        l=0 #left pointer
        result = [] 
        win_dict ={}
        length=len(words[0])
        word_count=len(words)
        
        #first window
        for w in s[:len(word)]:
            if w in win_dict:
                win_dict[w]+=1
            else:
                win_dict[w]=1

        if win_dict==word_dict:
            flag=0
            appeared={}
            for i in range(l,length*word_count,length):
                w=s[i:i+length]
                if w in all_words:
                    appeared[w]= appeared.get(w,0) + 1
                    if appeared[w]<=all_words[w]:
                        flag+=1
            if flag==word_count:       
                result.append(l)
            
        for r in range(len(word),len(s)):
            c=s[r] # char at right
            #delete the char at left
            char_left = s[l]
            win_dict[char_left]-=1
            l+=1
            if win_dict[char_left]==0:
                del win_dict[char_left]
    
            #add char at right pointer
            if c in win_dict:
                win_dict[c]+=1
            else:
                win_dict[c]=1
            
            #check if 
            if win_dict==word_dict:
                #print(l,r+1,len(words[0]))
                flag=0
                length=len(words[0])
                word_count=len(words)
                appeared={}
                for i in range(l,r+1,length):
                    w=s[i:i+length]
                    if w in all_words:
                        appeared[w]= appeared.get(w,0) + 1
                        if appeared[w]<=all_words[w]:
                            flag+=1
                if flag==word_count:       
                    result.append(l)
        return result
            