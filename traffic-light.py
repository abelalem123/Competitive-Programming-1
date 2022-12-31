
def get_pos(color,target):
    #calculate all index of a char(e.g r) in a string e.g rrggy
    result=[]
    for i,c in enumerate(color):
        if c==target:
            result.append(i)
    return result
def find_distance(current_pos,green_pos,color_len):
    #calculate distance between two color indicies in a circular 
    ans=-color_len
    for cpos in current_pos:
        min_d=color_len+1
        for gpos in green_pos:
            if cpos > gpos:
                d=(gpos-cpos)+color_len
            else:
                d=gpos-cpos
            min_d=min(d,min_d) # minimum of distance between current color and many green indicies
        ans=max(ans,min_d) # max because we can't know on which current color we are in. max of min 
    return ans
def main():        
    n=int(input())
    for i in range(n):
        color_len, cur= input().split()
        col=input()
        current_pos=get_pos(col,cur)
        green_pos=get_pos(col,'g')
        ans= find_distance(current_pos,green_pos,int(color_len))
        print(ans)
main()
        
        
