class TrieNode:
    def __init__(self, val: str = ""):
        self.letters = {}
        self.word = False

class WordDictionary:

    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        curr = self.root

        for i in range(len(word)):
            if word[i] not in curr.letters:
                curr.letters[word[i]] = TrieNode()
            curr = curr.letters[word[i]]
        curr.word = True

    def search(self, word: str) -> bool:
        def dfs(root, index):
            for i in range(index, len(word)):
                letter = word[i]

                if letter == ".":
                    for sub in root.letters.values():
                        if dfs( sub, i+1):
                            return True
                    return False
                else:
                    if letter not in root.letters:
                        return False
                    root = root.letters[letter]
            return root.word
        return dfs(self.root, 0)
