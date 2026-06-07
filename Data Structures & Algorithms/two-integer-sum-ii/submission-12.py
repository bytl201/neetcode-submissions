class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        left = 0
        right = len(numbers)-1

        while left < right:
            left_val = numbers[left]
            right_val = numbers[right]

            total = left_val + right_val

            if total < target:
                left +=1
            elif total > target:
                right -=1
            else:
                return [left+1, right+1]
            