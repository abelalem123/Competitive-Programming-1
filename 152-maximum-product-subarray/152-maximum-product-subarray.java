class Solution {
    public int maxProduct(int[] nums) {
        int upto_max=1;
        int upto_min=1;
        int absolute_max=nums[0];
        for (int num:nums){
                int tempmin=num*upto_min;
                int tempmax=num*upto_max;
                upto_max=Math.max(Math.max(tempmin,tempmax),num);
                upto_min=Math.min(Math.min(tempmin,tempmax),num);
                absolute_max=Math.max(absolute_max,upto_max);
        
    }
        return absolute_max;
    }
}