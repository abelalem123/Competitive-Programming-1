class Solution {
    public int longestConsecutive(int[] nums) {
        Set<Integer> num_set=new HashSet<Integer>();
        for (int num: nums ){
            num_set.add(num);
        }
        int max_count=0;
        for (int num: num_set){
            if (!num_set.contains(num-1)){
                int count=1;
                int curr=num;
                while(num_set.contains(num+1)){
                    num+=1;
                    count+=1;
                }
                max_count=Math.max(max_count, count);
            }
        }
        return max_count;
    }
}