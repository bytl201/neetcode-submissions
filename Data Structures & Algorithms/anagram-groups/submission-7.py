class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        final_list = defaultdict(list)

        for i in strs:
            abc_list = [0] * 26

            for j in i:
                abc_list[ord(j)-ord('a')] += 1

            final_list[tuple(abc_list)].append(i)
        return list(final_list.values())
