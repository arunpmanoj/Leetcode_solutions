import string
vowels = ['a', 'e', 'i', 'o', 'u' ,'A','E','I','O','U']
consonants= [ch for ch in string.ascii_letters if ch not in vowels]
digits = list(string.digits)
punctuation = list(string.punctuation)
class Solution:
    def isValid(self, word: str) -> bool:
        n=len(word)
        if n<3:
            return False
        has_vowels = False
        has_consonants = False
        has_punctuation = True

        for ch in word :
            if ch in vowels:
                has_vowels = True
            elif ch in consonants:
                has_consonants = True
            elif ch in punctuation:
                has_punctuation = False
        return has_vowels and has_consonants and has_punctuation