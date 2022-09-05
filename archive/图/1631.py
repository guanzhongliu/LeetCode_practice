'''
你准备参加一场远足活动。给你一个二维 rows x columns 的地图 heights ，其中 heights[row][col] 表示格子 (row, col) 的高度。
一开始你在最左上角的格子 (0, 0) ，且你希望去最右下角的格子 (rows-1, columns-1) （注意下标从 0 开始编号）。
你每次可以往 上，下，左，右 四个方向之一移动，你想要找到耗费 体力 最小的一条路径。
一条路径耗费的 体力值 是路径上相邻格子之间 高度差绝对值 的 最大值 决定的。
请你返回从左上角走到右下角的最小 体力消耗值 。

策略：（1）最短路，dijktra （2）并查集，按边由小到大排序，逐个增加，直到连通，连通的边的边长就是答案 (有趣的思路)
'''
from typing import List


class UnionFind:
    def __init__(self, n: int):
        self.head = list(range(n))
        self.size = [1] * n
        self.n = n
        self.setCount = n
    
    def find(self, x: int) -> int:
        if self.head[x] == x:
            return x
        self.head[x] = self.find(self.head[x])
        return self.head[x]
    
    def unite(self, x: int, y: int) -> bool:
        x, y = self.find(x), self.find(y)
        if x == y:
            return False
        if self.size[x] < self.size[y]:
            x, y = y, x
        self.head[y] = x
        self.size[x] += self.size[y]
        self.setCount -= 1
        return True
    
    def connected(self, x: int, y: int) -> bool:
        return self.find(x) == self.find(y)


class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        m, n = len(heights), len(heights[0])
        edges = list()
        for i in range(m):
            for j in range(n):
                iden = i * n + j
                if i > 0:
                    edges.append((iden - n, iden, abs(heights[i][j] - heights[i - 1][j])))
                if j > 0:
                    edges.append((iden - 1, iden, abs(heights[i][j] - heights[i][j - 1])))
        
        edges.sort(key=lambda e: e[2])

        uf = UnionFind(m * n)
        ans = 0
        for x, y, v in edges:
            uf.unite(x, y)
            if uf.connected(0, m * n - 1):
                ans = v
                break
        
        return ans
