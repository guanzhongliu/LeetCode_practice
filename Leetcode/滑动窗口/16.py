'''
给定一个包括 n 个整数的数组 nums 和 一个目标值 target。
找出 nums 中的三个整数，使得它们的和与 target 最接近。返回这三个数的和。假定每组输入只存在唯一答案。

策略: 
'''
from typing import List


class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        