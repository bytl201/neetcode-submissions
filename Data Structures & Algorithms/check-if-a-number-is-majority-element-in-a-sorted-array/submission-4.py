class Solution:
    def isMajorityElement(self, nums: List[int], target: int) -> bool:
        left = 0
        right = len(nums) - 1
        
        found = False
        while left <= right:
            middle = (left+right)//2

            if nums[middle] == target:
                found = True
                while middle > 0 and nums[middle-1] == target:
                    middle = middle - 1
                left = middle
                break
            elif nums[middle] > target:
                right = middle - 1
            elif nums[middle] < target:
                left = middle + 1
        
        if not found:
            return False

        count = 0
        while left <= len(nums)-1 and nums[left] == target:

            count += 1
            left += 1
        
        return True if count > (len(nums)/2) else False