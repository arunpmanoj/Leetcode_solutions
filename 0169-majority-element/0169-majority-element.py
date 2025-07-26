class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        n=len(nums)
        ele1=-1
        cnt=0
        for ele in nums:
            if ele1==ele:
                cnt +=1
            elif cnt==0:
                ele1=ele
                cnt +=1
            else:
                cnt-=1
        cnt=0
        for ele in nums:
            if ele1==ele:
                cnt +=1
        if cnt>len(nums)//2:
            return ele1