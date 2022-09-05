'''
Move Zeroes

Given an integer array nums, move all 0's to the end of it 
while maintaining the relative order of the non-zero elements.

Note that you must do this in-place without making a copy of the array.

Example 1:
Input: nums = [0,1,0,3,12]
Output: [1,3,12,0,0]

Example 2:
Input: nums = [0]
Output: [0]

Follow up: Could you minimize the total number of operations done?
'''


class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        # 遍历两次，第一次确定有多少个非零然后，第二次按顺序写入，最后末尾清零
        non_zero_num = 0
        for i in nums:
            if i != 0:
                non_zero_num += 1
        l = len(nums)
        cur_pos = 0
        for i in range(0, l):
            if nums[i] != 0:
                nums[cur_pos] = nums[i]
                cur_pos += 1
            if cur_pos >= non_zero_num:
                break
        for i in range(non_zero_num, l):
            nums[i] = 0

        '''
        另一种思路
        
        l = 0 # 标记哪里之前都是按顺序写入的
        
        for r in range(len(nums)):
            # 如果不是0, 就向前交换
            if nums[r]:
                nums[l], nums[r] = nums[r], nums[l]
                l += 1
        
        '''

        return nums

