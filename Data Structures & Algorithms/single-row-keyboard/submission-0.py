class Solution:
    def calculateTime(self, keyboard: str, word: str) -> int:
        result = 0
        last_char = keyboard[0]

        for char in word:
            print(last_char, char, keyboard.index(last_char), keyboard.index(char))
            time = abs(keyboard.index(last_char) - keyboard.index(char))
            result += time
            last_char = char
        
        return result