'''
Remove Duplicates from Sorted Array
Given an integer array nums sorted in non-decreasing order,
remove the duplicates in-place such that each unique element appears only once. 
The relative order of the elements should be kept the same.

Since it is impossible to change the length of the array in some languages, 
you must instead have the result be placed in the first part of the array nums. 
More formally, if there are k elements after removing the duplicates, 
then the first k elements of nums should hold the final result. 
It does not matter what you leave beyond the first k elements.

Return k after placing the final result in the first k slots of nums.

Do not allocate extra space for another array. 
You must do this by modifying the input array in-place with O(1) extra memory.

Example:

Input: nums = [0,0,1,1,1,2,2,3,3,4]
Output: 5, nums = [0,1,2,3,4,_,_,_,_,_]

'''


class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        # 双指针

        pos1 = 0    # 到这里为止是不重复的
        pos2 = 0    # 遍历整个list

        l = len(nums)

        while pos2 < l:
            if nums[pos2] > nums[pos1]:
                pos1 += 1
                nums[pos1], nums[pos2] = nums[pos2], nums[pos1]
            pos2 += 1

        return pos1 + 1
