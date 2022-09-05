'''
给你一个 32 位的有符号整数 x ，返回 x 中每位上的数字反转后的结果。
如果反转后整数超过 32 位的有符号整数的范围 [−2^31,  2^31 − 1] ，就返回 0。
假设环境不允许存储 64 位整数（有符号或无符号）。

策略
'''
class Solution:
    def reverse(self, x: int) -> int:
        maxbound = (1 << 31) - 1
        res = 0
        flag = 1
        if x < 0:
            x = -x
            flag = -1
        while x != 0:
            last = x % 10
            x = int(x / 10)
            if flag > 0 and (res > (maxbound // 10) or (res == (maxbound // 10) and last > 7)):
                return 0
            if flag < 0 and (res > (maxbound // 10) or (res == (maxbound) // 10 and last > 8)):
                return 0
            res = res * 10 + last
        return res * flag

s = Solution()
x = 1563847412
print(s.reverse(x))
