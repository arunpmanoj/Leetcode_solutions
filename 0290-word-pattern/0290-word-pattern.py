class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:

        d1={}
        d2={}
        s=s.split()
        if len(pattern) != len(s):
            return False
        for i,j in zip(pattern,s):
            if i not in d1:
                d1[i]=j
            elif d1[i]!=j:
                return False
            if j not in d2:
                d2[j]=i
            elif d2[j]!=i:
                return False
        return True  

        # cnt=0
        # for i in range(len(pattern)):
        #     if pattern[i]=="a" and s[i]=="dog":
        #         cnt+=1
        #     if pattern[i]=="b" and s[i]=="cat":
        #         cnt+=1
        # return True if cnt==len(pattern) else False