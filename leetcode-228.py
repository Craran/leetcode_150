from typing import List
class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        if not nums:
            return []
        i = j = 0
        result: List[int] = []
        ans: List[str] = []

        while True:
            if j + 1 == len(nums):
                result.append(nums[i: j + 1])
                break
            if nums[j + 1] == nums[i] + j - i + 1:
                j += 1
            else:
                result.append(nums[i: j + 1])
                i = j = j + 1

        def trans(input:List[int]) -> str:
            if len(input) == 1:
                return str(input[0])
            else:
                return str(input[0]) + '->' + str(input[-1])
            

        ans = list(map(trans, result))
        return ans