class Solution:
    def trap(self, height: List[int]) -> int:
        left_index = 0
        right_index = len(height) -1

        left_val = height[left_index]
        right_val = height[right_index]

        total = 0

        while left_index < right_index:
            if height[left_index] < height[right_index]:
                left_index +=1
                left_val = max(left_val, height[left_index])
                total += left_val - height[left_index]
            else:
                right_index -=1
                right_val = max(right_val, height[right_index])
                total += right_val - height[right_index]
        return total
