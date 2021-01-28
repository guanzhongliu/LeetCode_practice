'''
给定一个排序好的数组 arr ，两个整数 k 和 x ，从数组中找到最靠近 x（两数之差最小）的 k 个数。返回的结果必须要是按升序排好的。

整数 a 比整数 b 更接近 x 需要满足：

|a - x| < |b - x| 或者
|a - x| == |b - x| 且 a < b

策略: （1）两遍快排（复杂度最高，但代码好写）O(NlogN) （2）双指针 O(N) （3）二分查找 O(logN)
'''
from typing import List


class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        arr.sort(key=lambda s: abs(s - x))
        arr = sorted(arr[:k])
        return arr
    
    def findClosestElements_two_pointer(self, arr: List[int], k: int, x: int) -> List[int]:
        p1, p2 = 0, len(arr) - 1
        while p2 - p1 + 1 > k:
            if abs(arr[p1] - x) > abs(arr[p2] - x):
                p1 += 1
            else:
                p2 -= 1
        return arr[p1: p2 + 1]

    def findClosestElements_binary_search(self, arr: List[int], k: int, x: int) -> List[int]:
        size = len(arr)
        left = 0
        right = size - k

        while left < right:
            mid = (left + right) >> 1
            # 尝试从长度为 k + 1 的连续子区间删除一个元素
            # 从而定位左区间端点的边界值
            if x - arr[mid] > arr[mid + k] - x:
                left = mid + 1
            else:
                right = mid
        return arr[left:left + k]
