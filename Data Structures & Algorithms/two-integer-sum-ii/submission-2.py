class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        index1, index2 = 0, len(numbers) - 1 
        while index1 < index2:
            curr = numbers[index1] + numbers[index2]
            if curr == target:
                return [index1 + 1, index2 + 1]
            elif curr > target:
                index2 -= 1
            else:
                index1 += 1