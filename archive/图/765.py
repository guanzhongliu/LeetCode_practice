'''
N 对情侣坐在连续排列的 2N 个座位上，想要牵到对方的手。 计算最少交换座位的次数，以便每对情侣可以并肩坐在一起。 一次交换可选择任意两人，让他们站起来交换座位。

人和座位用 0 到 2N-1 的整数表示，情侣们按顺序编号，第一对是 (0, 1)，第二对是 (2, 3)，以此类推，最后一对是 (2N-2, 2N-1)。

这些情侣的初始座位  row[i] 是由最初始坐在第 i 个座位上的人决定的。

策略： BFS，计算连通分支，每个连通分支的大小-1的和即为答案
'''
from typing import List
import collections


class Solution:
    def minSwapsCouples(self, row: List[int]) -> int:
        l = len(row)
        vis = set()
        ans = 0
        edges = collections.defaultdict(list)
        for i in range(0, l, 2):
            edges[int(row[i]//2)].append(int(row[i + 1]//2))
            edges[int(row[i + 1]//2)].append(int(row[i]//2))
        for i in range(l//2):
            candidate = collections.deque()
            if i not in vis:
                vis.add(i)
                candidate.append(i)
                cnt = -1
                while len(candidate) != 0:
                    temp = candidate.popleft()
                    cnt += 1
                    for node in edges[temp]:
                        if node not in vis:
                            vis.add(node)
                            candidate.append(node)
                ans += cnt
        return ans


solution = Solution()
print(solution.minSwapsCouples([0, 2, 1, 3]))
