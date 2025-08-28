class Solution:
    def maxSum(self, nums: List[int]) -> int:
        nums=set(nums)
        max_num=max(nums)
        if max_num<0:
            return max_num
        else:
            return sum(x for x in nums if x >= 0)