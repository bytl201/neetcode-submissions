class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        group = defaultdict(list)

        for i in strs:
            abc_position = [0] * 26

            for j in i:
                abc_position[ord(j) - ord('a')] += 1

            group[tuple(abc_position)].append(i)

        return list(group.values())