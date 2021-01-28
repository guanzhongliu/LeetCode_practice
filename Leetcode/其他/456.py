'''
给定一个整数序列：a1, a2, ..., an，一个132模式的子序列 ai, aj, ak 被定义为：
当 i < j < k 时，ai < ak < aj。设计一个算法，当给定有 n 个数字的序列时，验证这个序列中是否含有132模式的子序列。

策略：栈结构！一个栈保留最小值
'''
from typing import List
import collections

class Solution:
    def find132pattern(self, nums: List[int]) -> bool:
        if len(nums) < 3:
            return False

        maxList = []
        minList = [nums[0], ]  # 保留j位置前的最小值

        for i in range(1, len(nums)):
            minList.append(min(minList[i - 1], nums[i]))

        for j in range(len(nums) - 1, -1, -1):
            # 如果当前数字比minList[j]大
            if nums[j] > minList[j]:
                while maxList and maxList[-1] <= minList[j]:
                    maxList.pop()
                if maxList and maxList[-1] < nums[j]:
                    return True
                maxList.append(nums[j])
        return False