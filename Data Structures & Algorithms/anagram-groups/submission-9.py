class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        result = defaultdict(list)

        for i in strs:
            abc = [0] * 26

            for j in i:
                ascii_num = ord(j) - ord('a')

                abc[ascii_num] += 1

            result[tuple(abc)].append(i)

        return list(result.values())