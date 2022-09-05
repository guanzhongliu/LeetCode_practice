'''
给你一个仅由大写英文字母组成的字符串，你可以将任意位置上的字符替换成另外的字符，总共可最多替换 k 次。在执行上述操作后，找到包含重复字母的最长子串的长度。

注意：字符串长度 和 k 不会超过 104。

策略：（1）滑动窗口，但需要遍历字典最大值，比较慢
      (2)官方题解也是滑动窗口，每次右指针右移，如果区间仍然满足条件，那么左指针不移动，否则左指针至多右移一格，保证区间长度不减小。
         虽然这样的操作会导致部分区间不符合条件，即该区间内非最长重复字符超过了k个。但是这样的区间也同样不可能对答案产生贡献。
         当我们右指针移动到尽头，左右指针对应的区间的长度必然对应一个长度最大的符合条件的区间。
'''
import collections


class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        i, ans = 0, 0
        total = ('', 0)
        characters = collections.defaultdict(lambda : 0)
        for j in range(len(s)):
            characters[s[j]] += 1
            while j - i + 1 - max(characters.values()) > k:
                characters[s[i]] -= 1
                if characters[s[i]] == 0:
                    del characters[s[i]]
                i += 1
            ans = max(ans, j - i + 1)
        return ans
    
    def characterReplacement_official(self, s: str, k: int) -> int:
        num = [0] * 26
        n = len(s)
        maxn = left = right = 0

        while right < n:
            print(num, left, right)
            num[ord(s[right]) - ord("A")] += 1
            maxn = max(maxn, num[ord(s[right]) - ord("A")])
            if right - left + 1 - maxn > k:
                num[ord(s[left]) - ord("A")] -= 1
                left += 1
            right += 1
        
        return right - left
s = "ABBBBBACDEFGHIJK"
k = 2
solution = Solution()
solution.characterReplacement_official(s, k)