class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False  # must be same length

        count = {}

        # Step 1: count letters in s
        for c in s:
            if c in count:
                count[c] += 1
            else:
                count[c] = 1

        # Step 2: subtract using t
        for c in t:
            if c not in count:
                return False  # extra letter in t
            
            count[c] -= 1

            if count[c] == 0:
                del count[c]  # clean up

        return len(count) == 0