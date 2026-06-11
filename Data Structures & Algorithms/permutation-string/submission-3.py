class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s1_len = len(s1)
        s2_len = len(s2)

        if s1_len > s2_len: return False

        s1_arr = [0] * 26
        s2_arr = [0] * 26


        for i in range(len(s1)):
            s1_arr[ord(s1[i])-ord('a')] += 1
            s2_arr[ord(s2[i])-ord('a')] += 1

        if s1_arr == s2_arr: return True

        left = 0
        for right in range(s1_len,len(s2)):
            # Add the new character on the right
            s2_arr[ord(s2[right]) - ord('a')] += 1
            
            # Remove the character on the left
            s2_arr[ord(s2[left]) - ord('a')] -= 1
            left += 1
            
            # Check if current window matches s1
            if s2_arr == s1_arr:
                return True
        return False