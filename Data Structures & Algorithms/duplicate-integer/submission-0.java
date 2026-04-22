class Solution {
    public boolean hasDuplicate(int[] nums) {
        int a=0;
        for(int i : nums){
            a++;
            for(int j=a;j<nums.length; j++){
                if(i==nums[j]){
                    return true;
                }
            }
        }
        return false;
    }
}
