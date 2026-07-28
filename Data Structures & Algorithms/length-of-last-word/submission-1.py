class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        stripped = s.split(" ")

        for i in range(len(stripped) - 1, -1, -1):
            print(stripped[i])
            if not stripped[i]:
                continue
            else:
                return len(stripped[i])
