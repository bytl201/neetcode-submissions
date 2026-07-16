class Solution:
    def calculateTime(self, keyboard: str, word: str) -> int:
        maps = {}
        for i,v in enumerate(keyboard):
            maps[v] = i

        result = 0
        last_char = keyboard[0]

        for char in range(len(word)):
            print(maps[last_char], maps[word[char]], word[char])

            time = abs(maps[last_char] - maps[word[char]])
            result += time
            last_char = word[char]
        
        return result