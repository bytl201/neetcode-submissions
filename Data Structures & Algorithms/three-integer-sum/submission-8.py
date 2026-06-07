class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()

        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            left = i +1
            right = len(nums) -1

            while left < right:
                l_val = nums[left]
                r_val = nums[right]

                total = nums[i] + l_val + r_val

                if total < 0:
                    left +=1
                elif total > 0:
                    right -=1
                else:
                    res.append([nums[i],l_val,r_val])
                    left +=1
                    while left < right and nums[left] == nums[left -1]:
                        left +=1

        return res