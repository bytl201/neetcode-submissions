class TrieNode:
    def __init__(self):
        self.letters = {}
        self.word = False

class WordDictionary:

    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        curr = self.root

        for char in word:
            if char not in curr.letters.keys():
                curr.letters[char] = TrieNode()
            curr = curr.letters[char]
        
        curr.word = True

    def search(self, word: str) -> bool:

        def dfs(node, index):
            if index == len(word):
                return node.word

            if word[index] == ".":
                for child in node.letters.values():
                    if dfs(child, index + 1):
                        return True
                return False

            else:
                if word[index] not in node.letters:
                    return False
                return dfs(node.letters[word[index]], index + 1)

        return dfs(self.root, 0)
