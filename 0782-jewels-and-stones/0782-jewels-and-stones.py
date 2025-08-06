class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        seen=set()
        cnt=0
        for stone in jewels:
            if stone not in seen:
                seen.add(stone)
        for stone in stones:
            if stone in seen:
                cnt+=1
        return cnt
        

