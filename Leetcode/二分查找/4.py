'''
给定两个大小为 m 和 n 的正序（从小到大）数组 nums1 和 nums2。请你找出并返回这两个正序数组的中位数。

进阶：你能设计一个时间复杂度为 O(log (m+n)) 的算法解决此问题吗？

策略：二分查找，分别在两个List进行二分查找考虑几种特殊情况即可
'''
from typing import List


class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        m = len(nums1)
        n = len(nums2)
        def getMedian(k):
            index1, index2 = 0, 0
            while True:
                if index1 == m:
                    return nums2[index2 + k - 1]
                if index2 == n:
                    return nums1[index1 + k - 1]
                if k == 1:
                    return min(nums1[index1], nums2[index2])
                
                newIndex1 = min(index1 + k // 2 - 1, m - 1)
                newIndex2 = min(index2 + k // 2 - 1, n - 1)
                
                if nums1[newIndex1] > nums2[newIndex2]:
                    k -= newIndex2 - index2 + 1
                    index2 = newIndex2 + 1
                else:
                    k -= newIndex1 - index1 + 1
                    index1 = newIndex1 + 1

        if (m + n) % 2 == 1:
            return getMedian((m + n + 1) // 2)
        else:
            return (getMedian((m + n)// 2) + getMedian((m + n) // 2 + 1)) / 2

s = Solution()
nums1 = [1,4]
nums2 = [2,3,5,6]
print(s.findMedianSortedArrays(nums1, nums2))