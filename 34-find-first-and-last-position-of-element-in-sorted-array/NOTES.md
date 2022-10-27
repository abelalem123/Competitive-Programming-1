Three binary searches
1) find first occurence(put the index at m) and break
2) find the left most index l=0 r=m, if found at mid, resize r=mid-1, and at last return l
3) to find the right most index l=m r=len(nums)-1, if found at mid, resize l=mid+1, and at last return r