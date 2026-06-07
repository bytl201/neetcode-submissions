class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        final_dict = defaultdict(list)

        for i in strs:
            abc_index = [0] * 26

            for j in i:

                abc_index[ord(j) - ord('a')] += 1

            final_dict[tuple(abc_index)].append(i)

        return list(final_dict.values())