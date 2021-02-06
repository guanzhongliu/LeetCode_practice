'''
给定 n 个整数，找出平均数最大且长度为 k 的连续子数组，并输出该最大平均数
策略：很简单
'''
from typing import List

class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        maxTotal = total = sum(nums[:k])
        n = len(nums)

        for i in range(k, n):
            total = total - nums[i - k] + nums[i]
            maxTotal = max(maxTotal, total)
        
        return maxTotal / k