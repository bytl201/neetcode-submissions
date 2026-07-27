class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2): return False

        s1_count= [0] * 26
        s2_count= [0] * 26

        for i in range(len(s1)):
            s1_ord = ord(s1[i]) - ord('a')
            s2_ord = ord(s2[i]) - ord('a')

            s1_count[s1_ord] += 1
            s2_count[s2_ord] += 1

        matches = 0
        for i in range(len(s1_count)):
            if s1_count[i] == s2_count[i]:
                matches += 1

        if matches == len(s1_count):
            return True

        left = 0
        for right in range(len(s1), len(s2)):

            right_ord = ord(s2[right]) - ord('a')
            s2_count[right_ord] += 1
 

            if s1_count[right_ord] + 1 == s2_count[right_ord]:
                matches -= 1
            elif s1_count[right_ord] == s2_count[right_ord]:
                matches += 1


            left_ord = ord(s2[left]) - ord('a')
            s2_count[left_ord] -= 1
            

            if s1_count[left_ord] - 1 == s2_count[left_ord]:
                matches -= 1
            elif s1_count[left_ord] == s2_count[left_ord]:
                matches += 1
            left += 1

            if matches == 26:
                return True
    
        return matches == 26

        