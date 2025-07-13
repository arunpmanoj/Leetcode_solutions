class Solution:
    def secondHighest(self, s: str) -> int:
        f_larg=s_larg=-1
        for ch in s:
            if ch.isdigit():
                num=int(ch)
                if num>f_larg:
                    s_larg=f_larg
                    f_larg=num
                elif num>s_larg and num!=f_larg:
                    s_larg=num
        return s_larg
