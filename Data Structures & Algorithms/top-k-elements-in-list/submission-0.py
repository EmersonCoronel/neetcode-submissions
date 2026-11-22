class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = {}
        for item in nums:
            if item in freq.keys():
                freq[item] += 1
            else:
                freq[item] = 1
        zipped = list(zip(freq.keys(), freq.values()))
        zipped.sort(key = lambda pair: pair[1], reverse = True)
        return [key for key, val in zipped[:k]]