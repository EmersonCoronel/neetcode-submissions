class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, mid, r, = 0, 0, len(nums) - 1
        if target not in nums:
            return -1
        if len(nums) == 1:
            return 0
        while (l < r):
            mid = (r + l) // 2
            if nums[mid] > nums[r]:
                l = mid + 1
            else:
                r = mid
        if l == 0:
            l, r = 0, len(nums) - 1
        elif target < nums[0]:
            l, r = l, len(nums) - 1
        else:
            l, r = 0, l
        while (l < r):
            mid = (r + l) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] > target:
                r = mid
            else:
                l = mid + 1
        return l