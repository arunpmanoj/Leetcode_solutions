class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        d1={}
        d2={}
        for i in nums1:
            d1[i] = 1 
        for i in nums2:
            d2[i] = 1 
        res = []
        for key in d1:
            if key in d2:
                res.append(key)
        return res



                       