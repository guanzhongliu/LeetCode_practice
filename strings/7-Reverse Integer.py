'''
Reverse Integer

Given a signed 32-bit integer x, return x with its digits reversed. 
If reversing x causes the value to go outside the signed 32-bit integer range [-2^31, 2^31 - 1], 
then return 0.

Assume the environment does not allow you to store 64-bit integers (signed or unsigned).

Example 1:
Input: x = 123
Output: 321

Example 2:
Input: x = -123
Output: -321

Example 3:
Input: x = 120
Output: 21

'''

class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        ans = 0
        sig = -1 if x < 0 else 1
        # 首先这里注意x可能是负数，是负数的话, (-1 // a) = -1, 所以要转换为正数
        x = abs(x)
        while x:
            ans = ans * 10 + x % 10
            x = x // 10
        ans = sig * ans
        # 注意这里题目要求要考虑溢出
        if ans < (-1 << 31) or ans >= (1 << 31):
            return 0
        else:
            return ans