class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        ele1=ele2=ele3= float('-inf')
        for i in nums:
            if i==ele1 or i==ele2 or i==ele3:
                continue
            if i>ele1:
                ele3=ele2
                ele2=ele1
                ele1=i
            elif i>ele2:
                ele3=ele2
                ele2=i
            elif i>ele3:
                ele3=i
        if ele3==float('-inf'):
            return ele1
        else:
            return ele3

       
            
        