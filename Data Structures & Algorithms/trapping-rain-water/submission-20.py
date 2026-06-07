class Solution:
    def trap(self, height: List[int]) -> int:
        left = 0
        right = len(height) -1

        max_left = height[left]
        max_right = height[right]

        res= 0

        while left < right:
            if height[left] < height[right]:
                print(f"left before: {left}")
                left +=1
                print(f"left after: {left}")

                print(f"max_left before: {max_left}")
                max_left = max(max_left,height[left])
                print(f"max_left after: {max_left}")

                print(max_left-height[left])
                print()
                res += max_left - height[left]
            else:
                right -=1
                max_right = max(max_right, height[right])
                res += max_right - height[right]

        return res