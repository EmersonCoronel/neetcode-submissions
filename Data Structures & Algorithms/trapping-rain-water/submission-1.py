class Solution:
    def trap(self, height: List[int]) -> int:
        mapping = [[0] * len(height) for _ in range(max(height) + 1)]
        count = 0
        # build walls
        for i in range(len(height)):
            curr_height = height[i]
            for j in range(curr_height):
                mapping[j][i] = 1
        for row_index in range(len(mapping)):
            index = 1
            while index < len(mapping[row_index]) - 1:
                if mapping[row_index][index] != 1 and (mapping[row_index][index - 1] == 1 or mapping[row_index][index - 1] == 2):
                    if (self.check_right(mapping[row_index], index)):
                        mapping[row_index][index] = 2
                        count += 1
                index += 1
        return count

    def check_right(self, row: List[int], index):
        if index + 1 == len(row):
            return False
        if row[index + 1] == 1:
            return True
        else:
            return self.check_right(row, index + 1)

    