'''
两个整数的 汉明距离 指的是这两个数字的二进制数对应位不同的数量。

计算一个数组中，任意两个数之间汉明距离的总和。
'''
from typing import List


class Solution:
    def totalHammingDistance(self, nums: List[int]) -> int:
        n = len(nums)
        res = 0
        for i in range(32):
            cnt = 0
            for num in nums:
                # 统计每个数第i位上1的个数
                cnt += 1 & (num >> i)
            res += cnt * (n - cnt)
        return res