'''
给你一个长度为 n 的整数数组，请你判断在 最多 改变 1 个元素的情况下，该数组能否变成一个非递减数列。

我们是这样定义一个非递减数列的： 对于数组中所有的 i (0 <= i <= n-2)，总满足 nums[i] <= nums[i + 1]。

策略：遍历 + 贪心，进行遍历，贪心策略为出现降序则考虑将第一个数字转为第二个数字，
     但此时需要保证第一个数字转换后不会和前一个数字形成降序，否则需要将第二个数字转为第一个数字
'''
from typing import List


class Solution:
    def checkPossibility(self, nums: List[int]) -> bool:
        cnt, maxnum = 0, -float('inf')
        for i in range(len(nums) - 1):  
            x, y = nums[i], nums[i + 1]
            if y < x:
                cnt += 1
                if cnt > 1:
                    return False
                if i > 0 and y < nums[i - 1]:
                        nums[i + 1] = x

        return cnt >= 0


s = Solution()
nums = [1, 1, 2, 1, 2]
print(s.checkPossibility(nums))
