'''
给定一个非负索引 k，其中 k ≤ 33，返回杨辉三角的第 k 行。
'''
from typing import List


class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        ans = [1]
        for i in range(rowIndex):
            ans.append(int(ans[i] * (rowIndex - i) / (i + 1)))
        return ans