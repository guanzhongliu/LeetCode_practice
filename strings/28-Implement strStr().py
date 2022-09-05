'''
Implement strStr().

Given two strings needle and haystack, 
return the index of the first occurrence of needle in haystack, 
or -1 if needle is not part of haystack.

Clarification:
What should we return when needle is an empty string? 
This is a great question to ask during an interview.
For the purpose of this problem, 
we will return 0 when needle is an empty string. 
This is consistent to C's strstr() and Java's indexOf().

'''


class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        # 显然是kmp, 构建next数组
        '''
        重点："部分匹配值"就是"前缀"和"后缀"的最长的共有元素的长度。
        '''
        def build_next(s):
            nxt = [0]
            x = 1   # 当前位置
            now = 0     # "前缀"和"后缀"的最长的共有元素的长度
            while x < len(s):
                # 对当前位置元素和之前的下一个进行比较，如果匹配，共有元素增加
                if s[x] == s[now]:
                    now += 1
                    x += 1
                    nxt.append(now)
                # 如果不匹配，看共有串的"前缀"和"后缀"的最长的共有元素的长度
                elif now:
                    now = nxt[now-1]
                # 如果不匹配，且共有串是0，显然仍然是0
                else:
                    x += 1
                    nxt.append(0)
            return nxt

        nxt = build_next(needle)

        h_p = 0 # 主串
        n_p = 0 # 模式串
        while h_p < len(haystack):
            # 匹配上则移至下一位
            if haystack[h_p] == needle[n_p]:
                h_p += 1
                n_p += 1
            # 从前缀重新匹配
            elif n_p:
                n_p = nxt[n_p - 1]
            # 没有前缀，继续后移
            else:
                h_p += 1
            if n_p == len(needle):
                return h_p - n_p
        return -1
        
