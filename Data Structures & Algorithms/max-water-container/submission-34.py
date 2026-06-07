class Solution:
    def maxArea(self, heights: List[int]) -> int:
        left = 0
        right = len(heights) - 1

        maxi = 0
        while left < right:
            width = right - left
            length = min(heights[left], heights[right])
            area = width * length
            maxi = max(maxi, area)

            if heights[left] < heights[right]:
                left += 1
            else:
                right -= 1

        return maxi