class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        left = 0
        right = len(numbers)-1

        while left < right:
            left_num = numbers[left]
            right_num = numbers[right]

            total = left_num + right_num

            if total > target:
                right -=1
            elif total < target:
                left += 1
            else:
                return [left+1, right+1]

