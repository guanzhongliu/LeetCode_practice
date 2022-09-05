'''
有两种特殊字符。第一种字符可以用一比特0来表示。第二种字符可以用两比特(10 或 11)来表示。
现给一个由若干比特组成的字符串。问最后一个字符是否必定为一个一比特字符。给定的字符串总是由0结束。

策略：其实只是要看末尾0之前的1是奇数还是偶数个
'''
from typing import List


class Solution:
    def isOneBitCharacter(self, bits: List[int]) -> bool:
        l =len(bits)
        flag = 0
        if l == 1:
            return True
        l -= 2
        while l >= 0:
            if bits[l] == 1:
                flag += 1
            else:
                break
            l -= 1
        
        return 1 - flag % 2
