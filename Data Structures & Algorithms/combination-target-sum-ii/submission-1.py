class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []

        candidates.sort()

        def helper(index, current, total_sum):
            if total_sum == target:
                res.append(current.copy())
                return

            if index >= len(candidates) or total_sum > target:
                return

            current.append(candidates[index])
            helper(index+1, current, total_sum + candidates[index])
            current.pop()

            next_index = index + 1
            while next_index < len(candidates) and candidates[next_index] == candidates[index]:
                next_index += 1
            helper(next_index, current, total_sum)

        helper(0, [], 0)


        return res
