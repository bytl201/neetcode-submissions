class Solution:
    def scoreOfString(self, s: str) -> int:
        total = 0

        left, right = 0,1

        while right < len(s):
            print()
            total += abs(ord(s[left]) - ord(s[right]))
            left += 1
            right += 1
        return total