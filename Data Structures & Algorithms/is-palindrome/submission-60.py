class Solution:
    def isPalindrome(self, s: str) -> bool:
        left = 0
        right = len(s) - 1

        while left < right:
            if not self.valid(s[left]):
                left += 1
                continue
            elif not self.valid(s[right]):
                right -= 1
                continue
            else:
                if s[left].lower() != s[right].lower():
                    return False
                left += 1
                right -= 1

        return True

    def valid(self, s: str):
        return ord('a') <= ord(s.lower()) <= ord('z') or ord('0') <= ord(s) <= ord('9')