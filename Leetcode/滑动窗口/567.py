'''
给定两个字符串 s1 和 s2，写一个函数来判断 s2 是否包含 s1 的排列。

换句话说，第一个字符串的排列之一是第二个字符串的子串。

策略：（1）滑动窗口 + 用字典记录（此处利用了python中字典可以直接进行==比较）
      （2）滑动窗口，建立长度为26的cnt数组保存各个字母出现次数，
           在一个区间内统计[left, right]，每向右移动一次，就统计一次进入区间的字符x的次数，如果cnt[x] > 0，那么将左指针右移动，
           当[left, right]长度恰好为n时，就找到乐一个目标子串，因为通过此步骤可以保证不存在比原子串多出来的字母
'''
import collections


class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        l = len(s1)
        if l > len(s2):
            return False
        template = collections.defaultdict(lambda: 0)
        res = collections.Counter()
        for i in range(l):
            template[s1[i]] += 1
        for i in range(l):
            res[s2[i]] += 1
        if template == res:
            return True
        for j in range(l, len(s2)):
            res[s2[j - l]] -= 1
            res[s2[j]] += 1
            if res[s2[j - l]] == 0:
                del res[s2[j - l]]
            if res == template:
                return True

        return False
    
    def checkInclusion_official(self, s1: str, s2: str) -> bool:
        l = len(s1)
        if l > len(s2):
            return False
        cnt = [0] * 26
        for i in range(l):
            cnt[ord(s1[i]) - ord('a')] -= 1
        left = 0
        for right in range(len(s2)):
            x = ord(s2[right]) - ord('a')
            cnt[x] += 1
            while cnt[x] > 0:
                cnt[ord(s2[left]) - ord('a')] -= 1
                left += 1
            if right - left + 1 == l:
                return True
        return False

solution = Solution()
s1 = "aa"
s2 = "abababa"
print(solution.checkInclusion(s1, s2))
