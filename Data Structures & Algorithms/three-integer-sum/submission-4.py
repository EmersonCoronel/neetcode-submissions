class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        sols = []
        if len(nums) < 3:
            return sols
        outer_index = 0
        while outer_index < len(nums) - 2:
            inner_1, inner_2 = outer_index + 1, len(nums) - 1
            while inner_1 < inner_2:
                triple = sorted([nums[outer_index], nums[inner_1], nums[inner_2]])
                triple_sum = sum(triple)
                if triple_sum == 0 and triple not in sols:
                    sols.append(triple)
                elif triple_sum > 0:
                    inner_2 -= 1
                else:
                    inner_1 += 1
            outer_index += 1
        return sols