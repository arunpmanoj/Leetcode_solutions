class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        vowel = "aeiou"
        cnt, j = 0, 0
        max_cnt = 0
        for i in range(len(s)):
            if s[i] in vowel:
                cnt += 1
            if i - j + 1 > k:
                if s[j] in vowel:
                    cnt -= 1
                j += 1
            max_cnt = max(max_cnt, cnt)
        return max_cnt