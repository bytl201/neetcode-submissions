class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        count = defaultdict(list)
        for i in strs:
            res = [0] * 26
            for j in i:
                res[ord(j)-ord('a')] += 1
            count[tuple(res)].append(i)
        
        return list(count.values())