class Solution:
    def areSentencesSimilar(self, sentence1: List[str], sentence2: List[str], similarPairs: List[List[str]]) -> bool:
        if len(sentence1) != len(sentence2): return False

        mapping = defaultdict(set)

        for i in similarPairs:
            mapping[i[0]].add(i[1])
            mapping[i[1]].add(i[0])

        for i in range(len(sentence1)):
            word1 = sentence1[i]
            word2 = sentence2[i]

            similar_word1 = mapping[word1]
            similar_word2 = mapping[word2]

            print(word1, similar_word2)
            print(word2, similar_word1)
            print()

            if word1 == word2:
                continue
            elif word1 in similar_word2 or word2 in similar_word1:
                continue
            else:
                return False

        return True