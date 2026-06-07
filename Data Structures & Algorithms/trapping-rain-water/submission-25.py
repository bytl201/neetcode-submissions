class Solution:
    def trap(self, height: List[int]) -> int:
        max_left = height[0]
        left = [0] * len(height)

        for i in range(len(height)):
            max_left = max(max_left, height[i])
            left[i] = max_left
        
        max_right = height[len(height)-1]
        right = [0] * len(height)

        for i in range(len(height)-1,-1,-1):
            max_right = max(max_right, height[i])
            right[i] = max_right
        
        res = 0
        for i in range(len(height)):
            min_height = min(left[i], right[i])
            h = height[i]

            total = min_height - h

            if total > 0:
                res += total
        return res

