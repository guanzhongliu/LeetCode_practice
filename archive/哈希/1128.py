'''
给你一个由一些多米诺骨牌组成的列表 dominoes。

如果其中某一张多米诺骨牌可以通过旋转 0 度或 180 度得到另一张多米诺骨牌，我们就认为这两张牌是等价的。

形式上，dominoes[i] = [a, b] 和 dominoes[j] = [c, d] 等价的前提是 a==c 且 b==d，或是 a==d 且 b==c。

在 0 <= i < j < dominoes.length 的前提下，找出满足 dominoes[i] 和 dominoes[j] 等价的骨牌对 (i, j) 的数量。

策略: 遍历 哈希
'''
import collections
from typing import List
from collections import defaultdict

class Solution:
    def numEquivDominoPairs(self, dominoes: List[List[int]]) -> int:
        hist = collections.defaultdict(lambda : 0)
        ans = 0
        for dominoe in dominoes:
            dominoe = sorted(dominoe)
            if (dominoe[0], dominoe[1]) in hist:
                ans += hist[(dominoe[0], dominoe[1])]
            hist[(dominoe[0], dominoe[1])] += 1
        return ans
