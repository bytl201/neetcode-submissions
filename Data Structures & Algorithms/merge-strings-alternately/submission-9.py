class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        result = []
        index = 0

        while index < len(word1) and index <  len(word2):
            result.append(word1[index])
            result.append(word2[index])
            index += 1

        if index < len(word1):
            result.append(word1[index:])
        elif index < len(word2):
            result.append(word2[index:])
        
        return "".join(result)
