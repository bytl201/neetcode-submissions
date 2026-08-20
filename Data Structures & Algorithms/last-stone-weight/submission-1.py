class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:

        while len(stones) > 1:
            stones.sort()
            print(stones)

            x, y = stones[-2], stones[-1]
            print(x,y)
            stones.pop()
            stones.pop()
            print(stones)

            if x != y:
                res = abs(x-y)
                stones.append(res)
                print(stones)
                print()
        
        return stones[0] if stones else 0

            

