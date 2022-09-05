'''
Contains Duplicate

Given an integer array nums, 
return true if any value appears at least twice in the array, 
and return false if every element is distinct.


Example:
Input: nums = [1,1,1,3,3,4,3,2,4,2]
Output: true

'''

class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        # 遍历，用set保存出现过的数字
        s = set()
        for i in nums:
            if i not in s:
                s.add(i)
            else:
                return True
        return False




