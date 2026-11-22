class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        result = [0] * len(temperatures)
        index = len(temperatures) - 2
        stack = [[temperatures[len(temperatures) - 1], len(temperatures) - 1]]
        while index >= 0:
            count = 0
            pop_count = 0
            while len(stack) > 0 and temperatures[index] >= stack[len(stack) - 1][0]:
                popped = stack.pop(len(stack) - 1)
                count += result[popped[1]]
            if len(stack) == 0:
                result[index] = 0
            else:
                count += 1
                result[index] = count
            stack.append([temperatures[index], index])
            index -= 1
        return result