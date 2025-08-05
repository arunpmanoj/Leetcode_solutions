class Solution:
    def numOfUnplacedFruits(self, fruits: List[int], baskets: List[int]):
        seen=set()
        count = 0
        for i in range(len(fruits)):
            placed=False
            for j in range(len(baskets)):
                if fruits[i]<=baskets[j] and j not in seen: 
                    seen.add(j)
                    placed=True
                    break
            if not placed:
                count+=1
        return count
