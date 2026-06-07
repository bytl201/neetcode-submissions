class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []
        print(nums)

        for a in range(len(nums)):
            left = a + 1
            right = len(nums) - 1

            while left < right:
                
                total = nums[a] + nums[left] + nums[right]

                if total > 0:
                    right -= 1
                elif total < 0:
                    left += 1
                else:
                    answer = [nums[a], nums[left], nums[right]]
                    
                    if answer not in res:
                        res.append(answer)

                    left += 1

                    while left < right and nums[left] == nums[left-1]:
                        left += 1
        return res
