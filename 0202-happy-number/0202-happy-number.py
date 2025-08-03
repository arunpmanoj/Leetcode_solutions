class Solution:
    def isHappy(self, n: int) -> bool:
        d=set()
        while n!=1 and n not in d:
            d.add(n)
            summ=0
            while n>0:
                temp = n%10
                summ+=temp**2
                n=n//10
            n=summ
        return True if n==1 else False