class Solution:
    def isPalindrome(self, s: str) -> bool:
        left = 0
        right = len(s) - 1

        while left < right:
            if not self.isAlpha(s[left]):
                left += 1
            elif not self.isAlpha(s[right]):
                right -= 1
            else:
                if s[left].lower() != s[right].lower():
                    return False
                else:
                    left += 1
                    right -= 1
        return True
    def isAlpha(self, c):
        return ord('a') <= ord(c.lower()) <= ord('z') or ord('0') <= ord(c) <= ord('9')