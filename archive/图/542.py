'''
给定一个由 0 和 1 组成的矩阵，找出每个元素到最近的 0 的距离。
两个相邻元素间的距离为 1 。

策略：BFS, 也可以使用左上、右下两个方向的DP dist[i][j] = min(dist[i][j], dist[i-1][j] + 1) dist[i][j] = min(dist[i][j], dist[i][j-1] + 1) 
'''
from typing import List
import collections


class Solution:
    def updateMatrix(self, matrix: List[List[int]]) -> List[List[int]]:
        m, n = len(matrix), len(matrix[0])
        dist = [[0] * n for _ in range(m)]
        zeroes_pos = [(i, j) for i in range(m) for j in range(n) if matrix[i][j] == 0]
        q = collections.deque(zeroes_pos)
        seen = set(zeroes_pos)
        while q:
            i, j = q.popleft()
            for ni, nj in [(i - 1, j), (i + 1, j), (i, j - 1), (i, j + 1)]:
                if 0 <= ni < m and 0 <= nj < n and (ni, nj) not in seen:
                    dist[ni][nj] = dist[i][j] + 1
                    q.append((ni, nj))
                    seen.add((ni, nj))
        return dist