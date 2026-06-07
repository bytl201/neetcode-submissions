class Solution:
    def isValid(self, s: str) -> bool:
        parentheses = {'}':'{', ")": "(", ']':'['}
        res = []

        for i in s:
            if i in parentheses.keys():
                if res and parentheses[i] == res[-1]:
                    res.pop()
                else:
                    return False
                
            else:
                res.append(i)

        return True if len(res) == 0 else False

