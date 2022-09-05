'''
Rotate Array

Given an array, rotate the array to the right by k steps, where k is non-negative

Example 1:

Input: nums = [1,2,3,4,5,6,7], k = 3
Output: [5,6,7,1,2,3,4]
Explanation:
rotate 1 steps to the right: [7,1,2,3,4,5,6]
rotate 2 steps to the right: [6,7,1,2,3,4,5]
rotate 3 steps to the right: [5,6,7,1,2,3,4]

Follow up:
Try to come up with as many solutions as you can. There are at least three different ways to solve this problem.
Could you do it in-place with O(1) extra space?
'''


class Solution(object):
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: None Do not return anything, modify nums in-place instead.
        """

        def gcd(a, b):
            r = a % b
            while r:
                a = b
                b = r
                r = a % b
            return b

        l = len(nums)
        # 这里的思路是把list分割为大小为num的独立的块, 每次移动都可以以块为单位进行移动
        # |num|num|num|....|num|
        num = gcd(l, k)   
        move_num = l // num  # 这里是每个元素需要移动几次（也就是有几个块）
        for i in range(num):    # 从块内的第一个位置开始移动
            prev = nums[i]
            for j in range(move_num):   # 每个位置都要移动组数次
                tmp = nums[(i + (j + 1) * k) % l]
                nums[(i + (j + 1) * k) % l] = prev
                prev = tmp
