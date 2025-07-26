class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        d1,d2={},{}
        for ch in ransomNote:
            d1[ch]=d1.get(ch,0)+1
        for ch in magazine:
            d2[ch]=d2.get(ch,0)+1
        for ch in ransomNote: 
            if d1[ch] > d2.get(ch,0):
                return False
        return True
