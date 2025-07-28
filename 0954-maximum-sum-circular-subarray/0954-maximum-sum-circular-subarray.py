class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        totalsum,currminsum,currmaxsum=0,0,0
        minsum,maxsum=nums[0],nums[0]
        n=len(nums)
        for i in range(n):
            currmaxsum=max(currmaxsum+nums[i],nums[i])
            maxsum=max(maxsum,currmaxsum)
            currminsum=min(currminsum+nums[i],nums[i])
            minsum=min(minsum,currminsum)
            totalsum+=nums[i]
        normalsum=maxsum
        circularsum=totalsum-minsum
        if minsum==totalsum:
            return normalsum
        return max(circularsum,normalsum)