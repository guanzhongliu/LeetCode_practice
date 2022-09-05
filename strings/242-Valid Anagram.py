'''
Given two strings s and t, return true if t is an anagram of s, and false otherwise.

An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, 
typically using all the original letters exactly once.

Example 1:
Input: s = "anagram", t = "nagaram"
Output: true

Example 2:
Input: s = "rat", t = "car"
Output: false
'''


class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        l = len(s)
        # 长度肯定要一样
        if l != len(t):
            return False
        num_set = dict()
        # 存一下每个字母几次
        for i in s:
            num_set.setdefault(i, 0)
            num_set[i] += 1
        # 看看一不一样
        for i in t:
            if (i not in num_set) or (num_set[i] == 0):
                return False
            else:
                num_set[i] -= 1
        return True