class Solution:
    def trap(self, height: List[int]) -> int:
        left = 0
        right = len(height) -1

        left_value = height[left]
        right_value = height[right]

        total = 0

        while left < right:
            if left_value < right_value:
                left += 1
                left_value = max(left_value, height[left])

                total += left_value - height[left]
            else:
                right -= 1
                right_value = max(right_value, height[right])

                total += right_value - height[right]
                
        return total