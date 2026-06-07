class Solution:
    def isPalindrome(self, s: str) -> bool:

        if not s:
            return True
        left = 0
        right = len(s) -1

        while left < right:
            left_val = s[left]
            right_val = s[right]

            if not self.alphaNum(left_val.lower()):
                left += 1
            elif not self.alphaNum(right_val.lower()):
                right -= 1
            else:
                if left_val.lower() != right_val.lower():
                    return False
                left +=1
                right -=1

        return True

    def alphaNum(self, c):
        return ord('a') <= ord(c) <= ord('z') or  ord('0') <= ord(c) <= ord('9')