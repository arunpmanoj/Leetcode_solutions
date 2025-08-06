class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        jewelset=set(jewels)
        cnt=0
        for stone in stones:
            if stone in jewelset:
                cnt+=1
        return cnt
        

