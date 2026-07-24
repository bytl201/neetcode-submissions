class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count = {}
        longest, left, right = 0, 0, 0

        while right < len(s):
            count[s[right]] = count.get(s[right], 0) + 1
            print("right",s[right], right)

            while (right - left + 1) - max(count.values()) > k:
                count[s[left]] = count.get(s[left], 0) - 1
                left += 1
            longest = max(longest, (right-left+1))
            right += 1
        return longest