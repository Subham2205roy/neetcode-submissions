class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numset=set(nums)
        longest=0
        for i in nums:
            if i-1 not in nums:
                current_length=0
                while i+current_length in numset:
                    current_length+=1
                longest=max(current_length,longest)
        return longest
