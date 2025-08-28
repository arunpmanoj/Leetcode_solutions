class Solution:
    def maxSum(self, nums: List[int]) -> int:
        if max(nums)<0:
            return max(nums)
        else:
            nums=set(nums)
            return sum(x for x in nums if x >= 0)