class Solution:
    def maxArea(self, heights: List[int]) -> int:
        max_area = 0
        for index in range(len(heights) - 1):
            for inner_index in range(len(heights) - index):
                area = min(heights[index], heights[inner_index + index]) * (inner_index)
                if area > max_area:
                    max_area = area
        return max_area
