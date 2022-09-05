'''
给定两个正整数 x 和 y，如果某一整数等于 x^i + y^j，其中整数 i >= 0 且 j >= 0，那么我们认为该整数是一个强整数。
返回值小于或等于 bound 的所有强整数组成的列表。
你可以按任何顺序返回答案。在你的回答中，每个值最多出现一次。

策略：
'''
from typing import List
import math


class Solution:
    def powerfulIntegers(self, x: int, y: int, bound: int) -> List[int]:
        n = int(math.log(bound, x)) if x >= 2 else 0
        m = int(math.log(bound, y)) if y >= 2 else 0
        ans = set()
        for i in range(n + 1):
            for j in range(m + 1):
                temp = x ** i + y ** j
                if temp <= bound:
                    ans.add(temp)
        return list(ans)
