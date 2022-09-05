'''
对于非负整数 X 而言，X 的数组形式是每位数字按从左到右的顺序形成的数组。例如，如果 X = 1231，那么其数组形式为 [1,2,3,1]。
给定非负整数 X 的数组形式 A，返回整数 X+K 的数组形式。

策略：逐位计算而已, 同时遍历+K/10也可
'''
from typing import List


class Solution:
    def addToArrayForm(self, A: List[int], K: int) -> List[int]:
        temp = []
        while(K != 0):
            temp.insert(0, K % 10)
            K = int(K/10)
        K = temp
        if len(A) < len(K):
            A, K = K, A
        long_len, short_len = len(A), len(K)
        ans = []
        c = 0
        for i in range(1, long_len + 1):
            if i <= short_len:
                temp = A[long_len - i] + K[short_len - i] + c
                ans.insert(0, temp % 10)
                c = int(temp / 10)
            else:
                temp = A[long_len - i] + c
                ans.insert(0, temp % 10)
                c = int(temp / 10)
        if c != 0:
            ans.insert(0, c)
        return ans


solution = Solution()
print(solution.addToArrayForm([1, 2, 3, 4], 123))
