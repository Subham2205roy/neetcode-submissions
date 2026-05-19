class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        prefix_sum=0
        hash={0:1}
        count=0
        for i in range(len(nums)):
            prefix_sum+=nums[i]
            remove=prefix_sum-k
            count+=hash.get(remove,0)
            hash[prefix_sum]=hash.get(prefix_sum,0)+1
        return count
            
        