class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        
        #bubble sort        
#         for i in range(len(names)-1,-1,-1):
#             for j in range(1,i+1):
                
#                 if heights[j] > heights[j-1]:
#                     heights[j],heights[j-1]=heights[j-1],heights[j]
#                     names[j],names[j-1]=names[j-1],names[j]
#         #print(heights)

        #selection sort
        # for i in range(len(names)):
        #     max_num=max(heights[i:])
        #     max_index=heights.index(max_num)
        #     heights[i],heights[max_index]=heights[max_index],heights[i]
        #     names[i],names[max_index]=names[max_index],names[i]
        
        #insertion sort
        # for i in range(1,len(names)):
        #     j=i
        #     while j and heights[j] > heights[j-1]:
        #         heights[j],heights[j-1]=heights[j-1],heights[j]
        #         names[j],names[j-1]=names[j-1],names[j]  
        #         j-=1
        
        #counting sort
        height_name_idx ={height:name for height,name  in zip(heights,names)}
        min_num = min(heights)
        max_num = max(heights)
        count = [0 for i in range(min_num + max_num +1)]
        for h in heights:
            count[h + min_num]+=1
        pointer = len(heights)-1
        for i,n in enumerate(count):
            for c in range(n):
                names[pointer]= height_name_idx[i - min_num]
                pointer -=1
        return names