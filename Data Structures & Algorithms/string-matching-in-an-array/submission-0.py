class Solution:
    def stringMatching(self, words: List[str]) -> List[str]:
        arr = []
        for i in words:
            for j in words:
                if i == j:
                    continue

                if i in j:
                    arr.append(i)
                    break
                    
        return arr
