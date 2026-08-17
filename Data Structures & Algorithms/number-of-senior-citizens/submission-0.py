class Solution:
    def countSeniors(self, details: List[str]) -> int:
        count = 0

        for i in details:
            age = int(i[11:13])
            count += 1 if age > 60 else 0

        return count