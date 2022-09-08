'''
Given two sorted arrays nums1 and nums2 of size m and n respectively, 
return the median of the two sorted arrays.

The overall run time complexity should be O(log (m+n)).
'''


class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        # 要求O(log (m+n))，所以一定是要用二分
        '''
        这个思路没实现出来
        # x -> x1 x2 | x3 x4 x5 x6
        # y -> y1 y2 y3 y4 y5 | y6 y7 y8
        # 其实是需要保证两个list左侧数量和等于右侧数量和
        # x2 <= y6, y5 <= x3
        # 答案就是 avg(max(x2,y5),min(x3,y6))
        # 关键是如何找到分界点 => 在两个list中较短的list上做二分搜索 O(log(min(m,n)))
        '''
        # 实际使用切片分别二分求结果
        l = len(nums1) + len(nums2)
        if l % 2 == 1:
            return self.find_kth(nums1, nums2, l // 2 + 1)
        else:
            return (self.find_kth(nums1, nums2, l // 2) + self.find_kth(nums1, nums2, l // 2 + 1)) / 2

    def find_kth(self, a, b , k):
        # k是合并后位于第k个位置
        if not a:
            return b[k - 1]
        if not b:
            return a[k - 1]
        
        ia, ib = len(a) // 2, len(b) // 2
        xa, xb = a[ia], b[ib]
        # 重点是理解这里：
        # 情况分为： 
        # 1. 两边切片长度和大于k: 大于k说明，第k大的值一定不在结尾值较大的切片的右侧，这部分可以直接去掉
        # 2. 两边切片长度和等于k: 等于k说明，第k大的值一定不在结尾值较大的切片的左侧，这部分可以直接去掉
        # 3. 两边切片长度和小于k: 小于k同样说明，第k大的值一定不在结尾值较大的切片的左侧，这部分可以直接去掉
        if ia + ib <= k - 2:
            if xa > xb:
                return self.find_kth(a, b[ib + 1:], k - ib - 1)
            else:
                return self.find_kth(a[ia + 1:], b, k - ia - 1)
        else:
            if xa > xb:
                return self.find_kth(a[:ia], b, k)
            else:
                return self.find_kth(a, b[:ib], k)