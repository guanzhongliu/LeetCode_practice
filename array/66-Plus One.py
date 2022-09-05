'''
Plus One

You are given a large integer represented as an integer array digits, 
where each digits[i] is the ith digit of the integer. 
The digits are ordered from most significant to least significant in left-to-right order. 
The large integer does not contain any leading 0's.

Increment the large integer by one and return the resulting array of digits.

Example:

Input: digits = [9]
Output: [1,0]
Explanation: The array represents the integer 9.
Incrementing by one gives 9 + 1 = 10.
Thus, the result should be [1,0].

'''

class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        add_on = 1
        l = len(digits)
        # 改了一个小优化，直到没有进位为止, 但在leetcode上似乎不如直接循环
        i = l - 1
        while add_on and (i >= 0):
            digits[i] = digits[i] + add_on
            add_on = digits[i] // 10
            digits[i] %= 10
            i -= 1
        if add_on:
            digits.insert(0, 1)

        return digits
