class Solution:
    def minSetSize(self, arr: List[int]) -> int:
        count ={}
        for i in arr:
            if i in count:
                count[i]+=1
            else:
                count[i]=1
        n=0
        removed =0
        half=len(arr)//2
        for v,f in sorted(count.items(), key= lambda a:a[1], reverse=True):
            #print(v,n,f)
            if n<half:
                #print('here')
                n+=f
                removed+=1
            if n>=half:
                break
        return removed