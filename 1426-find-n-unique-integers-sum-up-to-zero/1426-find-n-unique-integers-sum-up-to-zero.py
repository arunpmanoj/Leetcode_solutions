class Solution:
    def sumZero(self, n: int) -> List[int]:
        res = []
        for i in range(1, n // 2 + 1):
            res.extend([i, -i])
        if n % 2 == 1:
            res.append(0)
        return res
        # res=[]
        # i=1
        # if n%2==0:
        #     while i<=n//2:
        #         res.append(i)
        #         res.append(-i)
        #         i+=1
        # else:
        #     while i<=n//2:
        #         res.append(i)
        #         res.append(-i)
        #         i+=1
        #     res.append(0)  
        # return res