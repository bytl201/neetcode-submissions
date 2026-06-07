class Solution:
    def maxArea(self, heights: List[int]) -> int:
        left = 0
        right = len(heights) -1

        max_streak = 0

        while left < right:
            total = min(heights[left], heights[right]) * (right - left)

            max_streak = max(max_streak, total)

            if heights[left] > heights[right]:
                right -=1
            else:
                left +=1

        return max_streak