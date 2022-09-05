'''
输入一个整数 n ，求1～n这n个整数的十进制表示中1出现的次数。
例如，输入12，1～12这些整数中包含1 的数字有1、10、11和12，1一共出现了5次。

策略: 模拟，将数字分为三部分，按位统计: 高位，当前位，低位
    三种情况 （1）当前位为0，这种情况当前位出现1的次数由高位 * 10^n 决定；
            （2）当前位为1，这种情况当前位出现1的次数由高位 * 10^n 和低位决定；
             (3) 当前位为2-9，这种情况当前位出现1的次数由（高位 + 1）* 10^n 决定

'''
class Solution:
    def countDigitOne(self, n: int) -> int:
        pos, ans = 1, 0
        high, cur, low = n // 10, n % 10, 0
        while high != 0 or cur != 0:
            if cur == 0:
                ans += high * pos
            elif cur == 1:
                ans += high * pos + low + 1
            else:
                ans += (high + 1) * pos
            low += cur * pos
            cur = high % 10
            high //= 10
            pos *= 10
        return ans


        