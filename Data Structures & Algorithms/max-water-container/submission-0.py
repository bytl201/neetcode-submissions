class Solution:
    def maxArea(self, heights: List[int]) -> int:

        most_water = 0

        for left in range(len(heights)):
            for right in range(left + 1, len(heights)):
                width = right - left
                height = heights[right] if heights[left] > heights[right] else heights[left]

                area = width * height

                most_water = max(most_water, area)

        return most_water