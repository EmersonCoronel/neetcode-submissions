class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        def hours_needed(k: int) -> int:
            return sum(math.ceil(p / k) for p in piles)
        low, high = 1, max(piles)
        mid = (high + low) // 2
        while (low < high):
            mid = (high + low) // 2
            if hours_needed(mid) <= h:
                high = mid
            else:
                low = mid + 1
        return low
