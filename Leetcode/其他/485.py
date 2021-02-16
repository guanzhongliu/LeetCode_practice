'''
给定一个二进制数组， 计算其中最大连续1的个数。
'''
from typing import List


class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        maxCount = count = 0
        for num in nums:
            if num == 1:
                count += 1
            else:
                count = 0
            maxCount = max(maxCount, count)
                
        return maxCount
