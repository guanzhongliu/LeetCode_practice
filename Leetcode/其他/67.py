'''
给你两个二进制字符串，返回它们的和（用二进制表示）。
输入为 非空 字符串且只包含数字 1 和 0。
策略：（1）模拟 （2）转换，位运算
'''
class Solution:
    def addBinary(self, a: str, b: str) -> str:
        la, lb = len(a), len(b)
        ans = ''
        i, j , carry = 1, 1, 0
        while i <= la or j <= lb:
            if i <= la and j <= lb:
                temp = int(a[-i]) + int(b[-j]) + carry
            elif i > la:
                temp = int(b[-j]) + carry
            elif j > lb:
                temp = int(a[-i]) + carry
            else:
                break
            ans = str(temp % 2) + ans
            carry = int(temp // 2)
            i += 1
            j += 1
        if carry != 0:
            ans = str(carry) + ans
        return ans
    
    def addBinary_bypos(self, a, b) -> str:
        x, y = int(a, 2), int(b, 2)
        while y:
            answer = x ^ y
            carry = (x & y) << 1
            x, y = answer, carry
        return bin(x)[2:]
s = Solution()
print(s.addBinary('10','11111111'))