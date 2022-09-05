'''
给你一个整数 n ，请你将 1 到 n 的二进制表示连接起来，并返回连接结果对应的 十进制 数字对 109 + 7 取余的结果。

策略：（1）模拟     
      (2) 数学方法 利用等比数列求和
          S = (2**k (u−1)v + (a−t)w − a)v 在计算 S 的同时需要维护后缀 0 的个数。
'''


class Solution:
    def concatenatedBinary(self, n: int) -> int:
        ans = 1
        for i in range(2, n + 1):
            ans = (ans << (len(bin(i)) - 2)) + i
            ans %= 1000000007
        return ans

solution = Solution()
print(solution.concatenatedBinary(12))