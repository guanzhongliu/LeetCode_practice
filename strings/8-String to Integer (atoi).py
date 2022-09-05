'''
Implement the myAtoi(string s) function, 
which converts a string to a 32-bit signed integer (similar to C/C++'s atoi function).

The algorithm for myAtoi(string s) is as follows:

1. Read in and ignore any leading whitespace.
2. Check if the next character (if not already at the end of the string) is '-' or '+'. 
Read this character in if it is either. 
This determines if the final result is negative or positive respectively. 
Assume the result is positive if neither is present.
3. Read in next the characters until the next non-digit character or the end of the input is reached.
The rest of the string is ignored.
4. Convert these digits into an integer (i.e. "123" -> 123, "0032" -> 32). 
If no digits were read, then the integer is 0. Change the sign as necessary (from step 2).
5. If the integer is out of the 32-bit signed integer range [-231, 231 - 1], 
then clamp the integer so that it remains in the range. 
Specifically, integers less than -231 should be clamped to -231, 
and integers greater than 231 - 1 should be clamped to 231 - 1.
6. Return the integer as the final result.

Note:
Only the space character ' ' is considered a whitespace character.
Do not ignore any characters other than the leading whitespace or the rest of the string after the digits.

'''


class Solution(object):
    def myAtoi(self, s):
        """
        :type s: str
        :rtype: int
        """
        sign_flag = False
        num_flag = False
        sign = 1
        ans = 0
        for i in range(len(s)):
            # 如果是数字，就进行拼接
            if s[i].isdigit():
                ans = ans * 10 + int(s[i])
                num_flag = True
            # 如果不是数字，输出当前结果
            elif sign_flag or num_flag:
                return max(-1 << 31, min(ans * sign, (1 << 31) - 1))
            # 如果第一位是符号，记录
            elif s[i] == '+' or s[i] == '-':
                sign = -1 if s[i] == '-' else 1
                sign_flag = True
            # 如果第一位是特殊符号，返回0
            elif s[i] != ' ':
                return 0
        return max(-1 << 31, min(ans * sign, (1 << 31) - 1))
