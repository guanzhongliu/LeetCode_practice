'''
Two Sum

Given an array of integers nums and an integer target, 
return indices of the two numbers such that they add up to target.

You may assume that each input would have exactly one solution, 
and you may not use the same element twice.

You can return the answer in any order.

Example:
Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].

Follow-up: Can you come up with an algorithm that is less than O(n2) time complexity?
'''

import enum


class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        num_dict = dict()
        for idx, num in enumerate(nums):
            num_dict[num] = idx
        # 这里其实简化了，因为exactly一个答案，且是按顺序遍历，所以不用担心数字出现两次导致的字典覆盖问题
        for idx, num in enumerate(nums):
            remain = target - num
            if (remain in  num_dict) and (idx != num_dict[remain]):
                return [idx, num_dict[remain]]