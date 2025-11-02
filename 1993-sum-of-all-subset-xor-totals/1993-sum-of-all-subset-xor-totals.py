class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        if not nums:
            return 0
        xor_sum = 0
        for num in nums:
            xor_sum |= num
        return xor_sum * (1 << (len(nums) - 1))