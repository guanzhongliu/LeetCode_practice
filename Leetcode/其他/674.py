'''
给定一个未经排序的整数数组，找到最长且 连续递增的子序列，并返回该序列的长度。

连续递增的子序列 可以由两个下标 l 和 r（l < r）确定，如果对于每个 l <= i < r，都有 nums[i] < nums[i + 1] ，那么子序列 [nums[l], nums[l + 1], ..., nums[r - 1], nums[r]] 就是连续递增子序列。

'''
from typing import List


class Solution:
    def findLengthOfLCIS(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        ans, count = 1, 1
        for i in range(1, len(nums)):
            if nums[i] > nums[i-1]:
                count += 1
            else:
                count = 1
            ans = max(ans, count)
        return ans
solution = Solution()
print(solution.findLengthOfLCIS([1,3,5,7]))