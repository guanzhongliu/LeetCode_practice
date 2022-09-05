'''
给定一个字符串，请你找出其中不含有重复字符的 最长子串 的长度。

策略：哈希集 去重
'''
import collections


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        i = ans = j = 0
        hist = set()
        for j in range(len(s)):
            if s[j] not in hist:
                hist.add(s[j])
            else:
                while s[j] in hist:
                    hist.remove(s[i])
                    i += 1
                hist.add(s[j])
            ans = max(ans, j - i + 1)
        return ans

solution = Solution()
print(solution.lengthOfLongestSubstring("abcacd"))
            