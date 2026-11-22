class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        i = 0
        while(i < len(nums)):
            newtarget = target - nums[i]
            if newtarget in nums[:i]:
                return [i, nums[:i].index(newtarget) + 1]
            elif newtarget in nums[i+1:]:
                return [i, nums[i+1:].index(newtarget) + i + 1]
            else:
                i += 1
        return None