class Solution:
    def isPalindrome(self, s: str) -> bool:

        if not s:
            return True
        left = 0
        right = len(s) -1

        while left < right:
            left_val = s[left].lower()
            right_val = s[right].lower()

            if not self.alphaNum(left_val):
                left += 1
            elif not self.alphaNum(right_val):
                right -= 1
            else:
                if left_val != right_val:
                    return False
                left +=1
                right -=1

        return True

    def alphaNum(self, c):
        return ord('a') <= ord(c) <= ord('z') or  ord('0') <= ord(c) <= ord('9')