'''
爱丽丝和鲍勃有不同大小的糖果棒：A[i] 是爱丽丝拥有的第 i 根糖果棒的大小，B[j] 是鲍勃拥有的第 j 根糖果棒的大小。

因为他们是朋友，所以他们想交换一根糖果棒，这样交换后，他们都有相同的糖果总量。（一个人拥有的糖果总量是他们拥有的糖果棒大小的总和。）

返回一个整数数组 ans，其中 ans[0] 是爱丽丝必须交换的糖果棒的大小，ans[1] 是 Bob 必须交换的糖果棒的大小。

如果有多个答案，你可以返回其中任何一个。保证答案存在。

策略：（1）哈希集  （2）双指针(慢)
'''
from typing import List


class Solution:
    def fairCandySwap(self, A: List[int], B: List[int]) -> List[int]:
        sumA, sumB = sum(A), sum(B)
        diff = (sumA - sumB)//2
        nums = set()
        for a in A:
            nums.add(a)
        for b in B:
            if b + diff in nums:
                return [b + diff, b]
        return [0, 0]
    
    def fairCandySwap_two_pointer(self, A: List[int], B: List[int]) -> List[int]:
        sumA, sumB = sum(A), sum(B)
        diff = (sumA - sumB)//2
        A.sort()
        B.sort()
        i, j, la, lb = 0, 0, len(A), len(B)
        while i < la and j < lb:
            curr = A[i] - B[j]
            if curr == diff:
                return(A[i], B[j])
            elif curr < diff:
                i += 1
            else:
                j += 1
        return [0, 0]
