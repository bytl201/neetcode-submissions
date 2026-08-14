class Solution:
    def areSentencesSimilar(self, sentence1: List[str], sentence2: List[str], similarPairs: List[List[str]]) -> bool:
        if len(sentence1) != len(sentence2): return False

        similarMatches = defaultdict(set)

        for i in similarPairs:
            similarMatches[i[0]].add(i[1])
            similarMatches[i[1]].add(i[0])

        for i in range(len(sentence1)):
            w1, w2 = sentence1[i], sentence2[i]
            if w1 != w2 and w2 not in similarMatches[w1]:
                return False
            
        return True