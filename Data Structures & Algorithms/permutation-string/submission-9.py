class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        elif s1 == s2:
            return True

        s1_count, s2_count = [0] * 26, [0] * 26

        for i in range(len(s1)):
            s1_count[ord(s1[i]) - ord('a')] += 1
            s2_count[ord(s2[i]) - ord('a')] += 1

        matches = 0

        for i in range(len(s1_count)):
            if s1_count[i] == s2_count[i]:
                matches += 1

        if matches == 26:
            return True

        left = 0
        for right in range(len(s1), len(s2)):
            index_right = ord(s2[right]) - ord('a')
            s2_count[index_right] += 1

            if s1_count[index_right] == s2_count[index_right]:
                matches += 1
            elif s1_count[index_right] + 1 == s2_count[index_right]:
                matches -= 1

            index_left = ord(s2[left]) - ord('a')
            s2_count[index_left] -= 1

            if s1_count[index_left] == s2_count[index_left]:
                matches += 1
            elif s1_count[index_left] - 1 == s2_count[index_left]:
                matches -= 1

            if matches == 26:
                return True

            left += 1
        return False