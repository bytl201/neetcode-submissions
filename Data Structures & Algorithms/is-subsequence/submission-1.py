class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        s_pointer = 0
        t_pointer = 0
        matches = 0

        if len(s) > len(t):
            return False

        while s_pointer < len(s) and t_pointer < len(t):
            print(s[s_pointer], t[t_pointer], end="\n\n")
            if s[s_pointer] == t[t_pointer]:
                matches += 1
                s_pointer += 1
            t_pointer += 1
        
        print(f"matches = {matches}")
        return True if matches == len(s) else False