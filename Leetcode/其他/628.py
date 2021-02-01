'''
给你一个整型数组 nums ，在数组中找出由三个数组成的最大乘积，并输出这个乘积。

思路：注意可能有正有负，所以需要选择最大的三个数和最小的两个负数
'''

from typing import List

class Solution:
    def maximumProduct(self, nums: List[int]) -> int:
        min1, min2 = [float('inf')] * 2
        max1, max2, max3 = [float('-inf')] * 3
        for num in nums:
            if num > max1:
                max1, max2, max3 = num, max1, max2
            elif num > max2:
                max2, max3 = num, max2
            elif num > max3:
                max3 = num
            if num < min1:
                min1, min2 = num, min1
            elif num < min2:
                min2 = num
        ans = max(max1 * max2 * max3, max1 * min1 * min2)
        return ans