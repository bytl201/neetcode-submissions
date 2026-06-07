class Solution:
    def isValid(self, s: str) -> bool:
        result = {'}': '{', ')': '(', ']':'['}
        
        valid = []

        for element in s:
            if element in result.keys():
                if valid and result[element] == valid[-1]:
                    valid.pop()
                else:
                    return False
            else:
                valid.append(element)


        print(valid)
            

        return True if not valid else False
            