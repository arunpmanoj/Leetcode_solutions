class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maxx=res=nums[0]
        for i in range(1,len(nums)):
            maxx= max(maxx+nums[i],nums[i])
            res = max(res,maxx)
        return res