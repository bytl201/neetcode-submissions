class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        print(nums)
        final = []

        for i in range(len(nums)):

            if i > 0 and nums[i] == nums[i-1]:
                continue
            
            left = i + 1
            right = len(nums) - 1

            while left < right:
                num = nums[i] + nums[left] + nums[right]
                if num < 0:
                    left += 1
                elif num > 0:
                    right -= 1
                else:
                    final.append([nums[i], nums[left], nums[right]])

                    left += 1
                    right -= 1

                    while left < right and nums[left] == nums[left - 1]:
                        left += 1

        return final

                
