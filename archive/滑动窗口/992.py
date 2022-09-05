'''
给定一个正整数数组 A，如果 A 的某个子数组中不同整数的个数恰好为 K，则称 A 的这个连续、不一定不同的子数组为好子数组。
（例如，[1,2,3,1,2] 中有 3 个不同的整数：1，2，以及 3。）
返回 A 中好子数组的数目。

策略：left1为到当前位置有K个数字的最远左区间，left2为到当前位置有K-1个数字的最远左区间，所以在lef1到left2的左闭右开的区间内
'''

from typing import List
import collections


class Solution:
    def subarraysWithKDistinct(self, A: List[int], K: int) -> int:
        num1, num2 = collections.Counter(), collections.Counter()
        tot1 = tot2 = 0
        left1 = left2 = 0
        ret = 0

        for num in A:
            if num1[num] == 0:
                tot1 += 1
            num1[num] += 1
            if num2[num] == 0:
                tot2 += 1
            num2[num] += 1
            
            while tot1 > K:
                num1[A[left1]] -= 1
                if num1[A[left1]] == 0:
                    tot1 -= 1
                left1 += 1
            while tot2 > K - 1:
                num2[A[left2]] -= 1
                if num2[A[left2]] == 0:
                    tot2 -= 1
                left2 += 1
            
            ret += left2 - left1
        
        return ret