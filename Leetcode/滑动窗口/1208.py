'''
给你两个长度相同的字符串，s 和 t。
将 s 中的第 i 个字符变到 t 中的第 i 个字符需要 |s[i] - t[i]| 的开销（开销可能为 0），也就是两个字符的 ASCII 码值的差的绝对值。
用于变更字符串的最大预算是 maxCost。在转化字符串时，总开销应当小于等于该预算，这也意味着字符串的转化可能是不完全的。
如果你可以将 s 的子字符串转化为它在 t 中对应的子字符串，则返回可以转化的最大长度。
如果 s 中没有子字符串可以转化成 t 中对应的子字符串，则返回 0。

策略：思路很简单，计算字符串各位之间的差值，将其转化为小于maxCost的最长子序列问题
'''


class Solution:
    def equalSubstring(self, s: str, t: str, maxCost: int) -> int:
        l = len(s)
        temp = []
        begin, cost, maxlen = 0, 0, 0
        for i in range(l):
            temp.append(abs(ord(s[i]) - ord(t[i])))
            cost += temp[i]
            if cost > maxCost:
                cost -= temp[begin]
                begin += 1
            else:
                maxlen = max(maxlen, i - begin + 1)
        return maxlen

solution = Solution()
s = "abcd"
t = "zzzz"
print(solution.equalSubstring(s, t, 3))