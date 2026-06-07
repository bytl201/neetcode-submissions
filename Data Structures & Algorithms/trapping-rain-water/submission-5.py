class Solution:
    def trap(self, height: List[int]) -> int:
        max_left = [0] * len(height)
        max_right = [0] * len(height)

        prefix = 0
        for i in range(len(height)):
            max_left[i] = prefix
            prefix = max(prefix, height[i])
        
        postfix = 0
        for i in range(len(height)-1,-1,-1):
            max_right[i] = postfix
            postfix = max(postfix, height[i])

        min_height = [0] * len(height)
        for i in range(len(height)):
            min_height[i] = min(max_left[i], max_right[i])
    
        res = 0
        for i in range(len(height)):
            print(min_height[i])
            print(height[i])
            print()
            num = min_height[i] - height[i]
            if num <= 0:
                continue
            else:
                res += num
        return res