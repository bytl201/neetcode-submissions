class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}

        for i in nums:
            count[i] = count.get(i,0) + 1

        print(count)

        arr = [[] for i in range(len(nums) + 1)]

        for v, c in count.items():
            arr[c].append(v)
        print(arr)

        answer = []
        for i in range(len(arr) - 1, 0, -1):
            print(i)
            for j in arr[i]:
                answer.append(j)
            if len(answer) >= k:
                return answer