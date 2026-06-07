class Solution:
    def isPalindrome(self, s: str) -> bool:
        left = 0
        right = len(s)-1

        while left < right:
            if not self.alphaNum(s[left]):
                left +=1
            elif not self.alphaNum(s[right]):
                right-=1
            else:
                if s[left].lower() != s[right].lower():
                    return False
                print('before')
                print(s[left])
                print(s[right])
                left+=1
                right-=1
                print('after')
                print(s[left])
                print(s[right])
                print()
        return True

    def alphaNum(self, c):
        return ord('a') <= ord(c) <= ord('z') or ord("A") <= ord(c) <= ord("Z") or ord("0") <= ord(c) <= ord("9")