class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = defaultdict(list)

        for i in strs:
            abc_position = [0] * 26

            for j in i:
                abc_position[ord(j)-ord("a")] += 1

            res[tuple(abc_position)].append(i)

        return list(res.values())