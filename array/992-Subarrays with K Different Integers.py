'''
Given an integer array nums and an integer k, return the number of good subarrays of nums.

A good array is an array where the number of different integers in that array is exactly k.

For example, [1,2,3,1,2] has 3 different integers: 1, 2, and 3.
A subarray is a contiguous part of an array.
'''

class Solution(object):
    def subarraysWithKDistinct(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        ptr = 0
        ans = 0
        accumulate = 1
        # 保存从 ptr 到 i 每个数字出现的次数
        num_dict = {}
        for i in range(len(nums)):
            if nums[i] not in num_dict:
                num_dict[nums[i]] = 1
            else:
                num_dict[nums[i]] += 1
            if len(num_dict) < k:
                continue
            elif len(num_dict) > k:
                accumulate = 1
                # 因为ptr保持在第一个unique的数字，所以这里可以直接右移一位,
                # 寻找新的组合
                num_dict[nums[ptr]] -= 1
                ptr += 1
                if num_dict[nums[ptr]] == 0:
                    del num_dict[nums[ptr]]
            # 这里是最关键的，相当于每移动一次右边界, 都要计算从ptr到i的所有子数组
            # 把ptr移动到第一个unique的数字
            while num_dict[nums[ptr]] > 1:
                num_dict[nums[ptr]] -= 1
                ptr += 1
                accumulate += 1
            ans += accumulate
        return ans
