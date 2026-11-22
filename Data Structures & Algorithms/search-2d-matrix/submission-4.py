class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        nums = matrix[0]
        for row in matrix:
            if target <= row[-1]:
                nums = row
                break
        l, r = 0, len(nums) - 1
        while (l <= r):
            m = (l + r) // 2
            if nums[m] < target:
                l = m + 1
            elif nums[m] > target:
                r = m - 1
            else:
                return True
        return False