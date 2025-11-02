class Solution:
    def maximumDifference(self, nums: List[int]) -> int:
        min_ele = nums[0]
        max_diff = -1
        for i in range(1, len(nums)):
            if nums[i] > min_ele:  
                diff = nums[i] - min_ele
                max_diff = max(max_diff, diff)
            else:
                min_ele = nums[i] 
        return max_diff
