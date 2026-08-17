class StringIterator:

    def __init__(self, compressedString: str):
        self.index = 0
        self.tokens = []
        i = 0
        while i < len(compressedString):
            char = compressedString[i]
            i += 1
            num_str = ""
            while i < len(compressedString) and compressedString[i].isdigit():
                num_str += compressedString[i]
                i += 1
            self.tokens.append([char, int(num_str)])

    def next(self) -> str:
        if self.hasNext():
            char = self.tokens[self.index][0]
            self.tokens[self.index][1] -= 1
            if self.tokens[self.index][1] == 0:
                self.index += 1
            return char
        return " "

    def hasNext(self) -> bool:
        return self.index < len(self.tokens)