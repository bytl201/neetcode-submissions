class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l = 0
        substring = set()
        long = 0

        for r in range(len(s)):
            while s[r] in substring:
                substring.remove(s[l])
                l += 1
            print(substring)
            substring.add(s[r])
            print(substring,end="\n\n")
            long = max(long, len(substring))

        return long