class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # 1. sort the arr
        # 2. one loop that will iterate until len(nums) - 2
        # 3. two pointers, one left that will be i+1 , one right end of the list
        # 4. check if num == 0 and add to res
        # 5. while loop to check if the next iteration of num is the same as the current num, so then skip left until new number or end of loop

        nums.sort()
        res = []

        for i in range(len(nums)-2):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            num = nums[i]
            left = i + 1
            right = len(nums) - 1

            while left < right:
                num_left = nums[left]
                num_right = nums[right]

                total = num + num_left + num_right

                if total == 0:
                    res.append([num, num_left, num_right])
                    left += 1
                    right -= 1
                    while left < right and nums[left] == nums[left - 1]:
                        left += 1
                    while left < right and nums[right] == nums[right + 1]:
                        right -= 1
                elif total < 0:
                    left += 1
                else:
                    right -= 1

        return res
