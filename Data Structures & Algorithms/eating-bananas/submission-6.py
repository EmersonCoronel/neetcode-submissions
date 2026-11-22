class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        def edible(k):
            total = 0
            for pile in piles:
                total += math.ceil(pile / k)
            if total <= h:
                return True
            return False
        
        l, k, r = 1, max(piles), max(piles)
        while l <= r:
            m = (l + r) // 2
            if edible(m):
                r = m - 1
                if m < k:
                    k = m
            else:
                l = m + 1
        return k
        