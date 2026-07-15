class Solution:
    def appendCharacters(self, s: str, t: str) -> int:
        i, j, matches = 0,0,0

        while i < len(s) and j < len(t):
            if s[i] == t[j]:
                matches += 1
                j += 1
            i += 1
        
        return len(t) - matches
