class Solution:
    def maxArea(self, heights: List[int]) -> int:
        max_area = 0

        for i in range(len(heights)):
            for j in range(i+1, len(heights)):
                width = j-i
                length = min(heights[i], heights[j])
                area = width * length

                max_area = max(max_area, area)

        return max_area
