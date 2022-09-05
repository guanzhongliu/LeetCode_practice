'''
「快乐前缀」是在原字符串中既是 非空 前缀也是后缀（不包括原字符串自身）的字符串。

给你一个字符串 s，请你返回它的 最长快乐前缀。

如果不存在满足题意的前缀，则返回一个空字符串。

策略：（1）Rabin-Karp 字符串编码：对于字符串包含的字符种类不超过k的情况，我们可以选择一个大于等于k的整数base，将字符串看作base进制的整数，
         将其再次转化为10进制后，就可以得到字符串对应的编码。
         但编码只可能很大，所以一般还要对一个数进行mod取模，但这样有一定几率会产生哈希碰撞，所以可以考虑选择多个模数如10^9+7或10^9+9，base一般选择质数
     （2）KMP

'''

class Solution:
    def longestPrefix(self, s: str) -> str:
        n = len(s)
        pre, tail = 0, 0
        base, mod, mul = 31, 1000000007, 1
        happy = 0
        for i in range(1, n):
            pre = (pre * base + ord(s[i-1]) - 97) % mod
            tail = (tail + (ord(s[n-i]) - 97) * mul ) % mod
            if pre == tail:
                happy = i
            mul = (mul * base) % mod
        return s[:happy]
    
    def longestPrefix_kmp(self, s: str) -> str:
        n = len(s)
        ntp = [-1] * n
        for i in range(1, n):
            j = ntp[i - 1]
            while j != -1 and s[j + 1] != s[i]:
                j = ntp[j]
            if s[j + 1] == s[i]:
                ntp[i] = j + 1
        return s[:ntp[-1] + 1]

solution = Solution()
s = 'bba'
print(solution.longestPrefix_kmp(s))    
