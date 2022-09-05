'''
A phrase is a palindrome if, after converting all uppercase letters into lowercase letters 
and removing all non-alphanumeric characters, it reads the same forward and backward. 
Alphanumeric characters include letters and numbers.

Given a string s, return true if it is a palindrome, or false otherwise.

Example 1:
Input: s = "A man, a plan, a canal: Panama"
Output: true
Explanation: "amanaplanacanalpanama" is a palindrome.

Example 2:
Input: s = "race a car"
Output: false
Explanation: "raceacar" is not a palindrome.

Example 3:
Input: s = " "
Output: true
Explanation: s is an empty string "" after removing non-alphanumeric characters.
Since an empty string reads the same forward and backward, it is a palindrome.
'''

class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        l = len(s)
        # 一头一尾
        pos1, pos2  = 0, l - 1
        while pos1 < pos2:
            # 跳过非数字字母，注意 isalnum可以判断是不是数字or字母
            while pos1 < l and (not s[pos1].isalnum()):
                pos1 += 1
            while pos2 >= 0 and (not s[pos2].isalnum()):
                pos2 -= 1
            # pos1要小于pos2
            if pos1 < pos2:
                if s[pos1].lower() == s[pos2].lower():
                    pos1 += 1
                    pos2 -= 1
                else:
                    return False
        return True
