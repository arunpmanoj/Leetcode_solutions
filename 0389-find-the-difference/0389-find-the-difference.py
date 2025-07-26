class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        d1={}
        d2={}
        for i in s:
            d1[i]=d1.get(i,0)+1
        for i in t:
            d2[i]=d2.get(i,0)+1
        for key in d2:
            if key not in d1 or d2[key] != d1[key]:
                return key
