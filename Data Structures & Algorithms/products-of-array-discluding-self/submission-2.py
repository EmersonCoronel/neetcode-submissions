class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        product_with_0 = 1
        product_no0 = 1
        count0 = 0
        for item in nums:
            product_with_0 *= item
            if item != 0:
                product_no0 *= item
            else:
                count0 += 1
        sol = [product_with_0] * len(nums)
        if count0 > 1:
            return sol
        index = 0
        while index < len(nums):
            if nums[index] == 0 and count0 == 1:
                sol[index] = product_no0
            else:
                sol[index] = int(sol[index] / nums[index])
            index += 1
        return sol