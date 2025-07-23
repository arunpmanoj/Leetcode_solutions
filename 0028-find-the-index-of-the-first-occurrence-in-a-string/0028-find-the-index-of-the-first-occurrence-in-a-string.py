class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if not needle:
            return 0

        n = len(needle)
        h = len(haystack)

        for i in range(h - n + 1):
            word = ""
            k = 0
            for j in range(i, i + n):
                if haystack[j] == needle[k]:
                    word += haystack[j]
                    k += 1
                else:
                    break
            if word == needle:
                return i
        return -1