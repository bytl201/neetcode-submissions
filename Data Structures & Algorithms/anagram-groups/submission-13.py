class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        count = defaultdict(list)
        freq = [[] for i in range(len(strs) + 1)]

        for i in strs:
            abc = [0] * 26

            for j in i:
                abc[ord(j)-ord('a')] +=1
            
            count[tuple(abc)].append(i)

        return list(count.values())