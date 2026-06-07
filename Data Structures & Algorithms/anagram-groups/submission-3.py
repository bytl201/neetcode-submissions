class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        final_list = defaultdict(list)

        for i in strs:

            ascii_list = [0] * 26
            for s in i:
                ascii_list[ord(s) - ord('a')] += 1

            final_list[tuple(ascii_list)].append(i)
    
        return list(final_list.values())