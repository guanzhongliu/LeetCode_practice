'''
给定一个整数类型的数组 nums，请编写一个能够返回数组 “中心索引” 的方法。

我们是这样定义数组 中心索引 的：数组中心索引的左侧所有元素相加的和等于右侧所有元素相加的和。

如果数组不存在中心索引，那么我们应该返回 -1。如果数组有多个中心索引，那么我们应该返回最靠近左边的那一个。

策略：前缀和
'''
from typing import List
import collections

class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        l = len(nums)
        if l < 1:
            return -1
        pre = [0] * l
        pre[0] = nums[0]
        for i in range(1, l):
            pre[i] = nums[i] + pre[i-1]
        for i in range(0, l):
            if pre[i]-nums[i] ==  pre[l-1] - pre[i]:
                return i
        return -1