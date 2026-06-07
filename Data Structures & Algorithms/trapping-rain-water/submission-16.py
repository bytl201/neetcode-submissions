class Solution:
    def trap(self, height: List[int]) -> int:
        left = [0] * len(height)
        right = [0] * len(height)

        prefix = 0
        for i in range(len(height)):
            left[i] = prefix
            prefix = max(prefix, height[i])

        postfix = 0
        for i in range(len(height)-1,-1,-1):
            right[i] = postfix
            postfix = max(postfix, height[i])

        print(left)
        print(right)

        res = 0

        for i in range(len(height)):
            total = min(left[i],right[i]) - height[i]

            if total > 0:
                res += total
            else:
                continue
        return res