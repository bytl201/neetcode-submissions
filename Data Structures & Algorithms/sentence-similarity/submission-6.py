class Solution:
    def areSentencesSimilar(self, sentence1: List[str], sentence2: List[str], similarPairs: List[List[str]]) -> bool:
        if len(sentence1) != len(sentence2): return False

        mapping = collections.defaultdict(set)

        for i in similarPairs:
            mapping[i[0]].add(i[1])
            mapping[i[1]].add(i[0])

        for i in range(len(sentence1)):
            word1 = sentence1[i]
            word2 = sentence2[i]
            if word1 == word2:
                continue
            
            elif word2 in mapping[word1] or word1 in mapping[word2]:
                continue
            else:
                return False

        return True