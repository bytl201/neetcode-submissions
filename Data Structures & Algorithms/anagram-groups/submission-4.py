class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # hold the final sublists with all the anagrams
        sublists = defaultdict(list)

        # iterating over each word
        for i in strs:

            # 26 positions in list to mimic the letters in the word
            letters_count = [0] * 26

            # iterating over each letter in the word
            for j in i:
                # adding 1 to letter position in list 
                letters_count[ord(j) - ord('a')] += 1

            # typecast to tuple to become a key
            # any words with the same letter positions will be appeneded to the same key (anagram)
            sublists[tuple(letters_count)].append(i)

        return list(sublists.values())
