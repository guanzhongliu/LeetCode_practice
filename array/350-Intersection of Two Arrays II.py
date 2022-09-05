'''
Intersection of Two Arrays II

Given two integer arrays nums1 and nums2, 
return an array of their intersection. 
Each element in the result must appear as many times as it shows in both arrays 
and you may return the result in any order.

Example:
Input: nums1 = [4,9,5], nums2 = [9,4,9,8,4]
Output: [4,9]
Explanation: [9,4] is also accepted.

'''

class Solution(object):
    def intersect(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        # 存下第一个list里每个数字出现几次
        num_dict = dict()
        for i in nums1:
            num_dict.setdefault(i, 0)
            num_dict[i] += 1
        res = []
        # 第二个如果出现一里且次数小于等于则加入结果
        for i in nums2:
            if (i in num_dict) and (num_dict[i] > 0):
                res.append(i)
                num_dict[i] -= 1
        return res