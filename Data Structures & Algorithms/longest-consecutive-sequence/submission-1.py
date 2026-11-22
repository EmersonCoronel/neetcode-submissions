class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums.sort()
        index, current, longest = 0, 1, 0
        prev = None
        while index < len(nums):
            if index != 0: 
                if nums[index] == prev + 1:
                    current += 1
                elif nums[index] != prev:
                    current = 1
            if current > longest:
                longest = current
            prev = nums[index]
            index += 1
        return longest