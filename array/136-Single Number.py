'''
Single Number

Given a non-empty array of integers nums, 
every element appears twice except for one. 
Find that single one.
You must implement a solution with a linear runtime complexity and use only constant extra space.

Example :

Input: nums = [4,1,2,1,2]
Output: 4
'''

class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # 思路很简单，任何一个数异或自己都为0，所以只需要将所有数一起异或
        ans = 0
        for i in nums:
            ans ^= i

        return ans