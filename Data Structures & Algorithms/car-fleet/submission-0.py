class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        times = [0] * len(position)
        count = 0
        combined = []
        for i in range(len(position)):
            combined.append([position[i], speed[i]])
        combined.sort()
        # print(combined)
        for i in range(len(combined)):
            index = len(combined) - 1 - i
            times[index] = (target - combined[index][0]) / combined[index][1]
            if index == len(combined) - 1:
                count += 1
            elif times[index] > times[index + 1]:
                count += 1
            else:
                times[index] = times[index + 1]
        return count