class Solution:
    def confusingNumber(self, n: int) -> bool:
        layout_valid = {0:0, 1:1, 6:9, 8:8, 9:6}
        layout_invalid = {2,3,4,5,7}

        str_n = str(n)

        sb = ""
        for i in range(len(str_n)-1,-1,-1):
            if int(str_n[i]) in layout_invalid:
                return False
            else:
                sb += str(layout_valid[int(str_n[i])])
        print(sb)
        
        if n != int(sb):
            return True
        else:
            return False