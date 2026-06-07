class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        index = min(len(word1), len(word2))

        res=""

        for i in range(index):
            res += word1[i] + word2[i]
        
        if len(word1) > len(word2):
            res += word1[index:]
        elif len(word1) < len(word2):
            res += word2[index:]
        
        return res