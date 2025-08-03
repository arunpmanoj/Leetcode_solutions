class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        d1={}
        d2={}
        for ch1,ch2 in zip(s,t):
            if ch1 not in d1:
                d1[ch1]=ch2
            elif d1[ch1]!=ch2:
                return False
            if ch2 not in d2:
                d2[ch2]=ch1
            elif d2[ch2]!=ch1:
                return False
        return True
            