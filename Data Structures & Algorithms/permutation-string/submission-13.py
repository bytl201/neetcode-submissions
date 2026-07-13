class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        
        s1_count, s2_count = [0] * 26, [0] * 26

        for i in range(len(s1)):
            s1_count[ord(s1[i]) - ord('a')] += 1
            s2_count[ord(s2[i]) - ord('a')] += 1

        matches = 0
        for i in range(len(s1_count)):
            if s1_count[i] == s2_count[i]:
                matches += 1
        
        if matches == 26: return True 
        
        left = 0

        for right in range(len(s1), len(s2)):
            r_index = ord(s2[right]) - ord('a')
            s2_count[r_index] += 1
            
            if s1_count[r_index] == s2_count[r_index]:
                matches += 1
            elif s1_count[r_index] == s2_count[r_index] - 1:
                matches -= 1
            
            l_index = ord(s2[left]) - ord('a')
            s2_count[l_index] -= 1

            if s1_count[l_index] == s2_count[l_index]:
                matches += 1
            elif s1_count[l_index] - 1 == s2_count[l_index]:
                matches -= 1
            
            print(s1_count)
            print(s2_count, end="\n\n")
            if matches == 26:
                return True
            left += 1

        return False