import string
punctuation = list(string.punctuation)
whitespace=[" "]
class Solution:
    def isPalindrome(self, s: str) -> bool:
        word=""
        for i in s:
            if i in punctuation or i in whitespace:
                word +=""
            elif i.isupper():
                i=i.lower()
                word +=i
            else:
                word+=i
        if word==word[::-1]:
            return True
        else:
            return False
        
             