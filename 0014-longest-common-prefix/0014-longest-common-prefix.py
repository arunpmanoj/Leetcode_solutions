class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        ref = strs[0]
        for i in range(len(ref)):
            ch = ref[i]
            for s in strs[1:]:
                if i >= len(s) or s[i] != ch:
                    return ref[:i]
        return ref