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
        def dfs(index, root):

            for i in range(index, len(word)):
                c = word[i]

                if c == ".":
                    for child in root.letters.values():
                        if dfs(i+1, child):
                            return True
                    return False

                else:
                    if c not in root.letters:
                        return False
                    root = root.letters[c]
            return root.word
        return dfs(0, self.root)