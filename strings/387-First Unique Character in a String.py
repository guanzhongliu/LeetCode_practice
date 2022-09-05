'''
First Unique Character in a String

Given a string s, find the first non-repeating character in it and return its index. 
If it does not exist, return -1.


Example 1:
Input: s = "leetcode"
Output: 0

Example 2:
Input: s = "loveleetcode"
Output: 2

Example 3:
Input: s = "aabb"
Output: -1

'''


class Solution(object):
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        num_set = dict()

        # 不要求空间复杂度的问题感觉都可以无脑dict/set
        for i in s:
            num_set.setdefault(i, 0)
            num_set[i] += 1

        for idx, i in enumerate(s):
            if num_set[i] == 1:
                return idx

        return -1
