class Solution:
    def makeFancyString(self, s: str) -> str:
        if len(s)<3:
            return s
        new =s[0]
        for i in range(1,len(s)-1):
            if s[i] == s[i-1] == s[i+1]:
                continue
            else:
                new+=s[i]
        new += s[-1]
        return new
       