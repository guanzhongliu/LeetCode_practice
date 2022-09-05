'''
给你一个由不同字符组成的字符串 allowed 和一个字符串数组 words 。如果一个字符串的每一个字符都在 allowed 中，就称这个字符串是 一致字符串 。

请你返回 words 数组中 一致字符串 的数目。

策略：按位转换，使用 & 和 ｜ 操作
'''

from typing import List

def word2int(word: str) -> int:
        ans = 0
        for a in word:
            ans |= (1 << (ord(a) - 97))
        return ans

class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        temp = word2int(allowed)
        ans = 0
        for word in words:
            t = word2int(word)
            if t & temp == t:
                ans += 1
        return ans

