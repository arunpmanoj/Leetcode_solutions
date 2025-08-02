class Solution:
    def firstUniqChar(self, s: str) -> int:
        d={}
        for char in s:
            if char not in d:
                d[char]=1
            else:
                d[char]=-1
        for key in d:
            if d[key]==1:
                return s.find(key)
        return -1
        # max_char=26
        # freq=[0]*26
        # for i in s:
        #     freq[ord(i)-ord('a')]+=1
        # for i in range(len(s)):
        #     if freq[ord(s[i])-ord('a')]==1:
        #         return i
        # return -1
