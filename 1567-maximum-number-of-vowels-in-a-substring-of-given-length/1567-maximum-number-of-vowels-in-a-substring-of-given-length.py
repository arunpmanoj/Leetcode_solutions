class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        vowels = 'aeiouAEIOU'
        cnt=0
        for i in s[:k]:
            if i in vowels:
                cnt+=1
        maxcnt=cnt
        for i in range(k,len(s)):
            if s[i] in vowels:
                cnt+=1
            if s[i-k] in vowels:
                cnt-=1
            if cnt>=maxcnt:
                maxcnt=cnt
        return maxcnt


                