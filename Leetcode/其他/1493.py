'''
给你一个二进制数组 nums ，你需要从中删掉一个元素。
请你在删掉元素的结果数组中，返回最长的且只包含 1 的非空子数组的长度。
如果不存在这样的子数组，请返回 0 。

策略：（1）遍历，需要考虑全是1的情况 （2）滑动窗口
'''
from typing import List


class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        now_len, length  = 0, len(nums)
        flag = 1
        lens = []
        for i in range(length):
            flag &= nums[i]
            if nums[i] == 1:
                now_len += 1
            if nums[i] == 0 or i == length - 1:
                lens.append(now_len)
                now_len = 0
        for i in range(len(lens) - 1, 0, -1):
            lens[i] += lens[i-1]
        return max(lens) - flag

class Solution_slide:
    def longestSubarray(self, nums: List[int]) -> int:
        last_len, now_len, length  = 0, 0, len(nums)
        ans = 0
        for i in range(length):
            if nums[i] == 1:
                now_len += 1
                last_len += 1
            if nums[i] == 0:
                last_len = now_len
                now_len = 0
            ans = max(last_len, ans)
        if ans == length:
            ans -= 1
        return ans

solution = Solution_slide()
print(solution.longestSubarray([1,0,1,0,0,1]))
            