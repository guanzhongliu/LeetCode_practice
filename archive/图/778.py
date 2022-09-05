'''
在一个 N x N 的坐标方格 grid 中，每一个方格的值 grid[i][j] 表示在位置 (i,j) 的平台高度。
现在开始下雨了。当时间为 t 时，此时雨水导致水池中任意位置的水位为 t 。
你可以从一个平台游向四周相邻的任意一个平台，但是前提是此时水位必须同时淹没这两个平台。
假定你可以瞬间移动无限距离，也就是默认在方格内部游动是不耗时的。当然，在你游泳的时候你必须待在坐标方格里面。
你从坐标方格的左上平台 (0，0) 出发。最少耗时多久你才能到达坐标方格的右下平台 (N-1, N-1)？

策略：BFS+优先队列    也可考虑： （1）二分查找+BFS  （2）并查集，按照时间模拟   （3）最短路 Dijkstra
'''
from typing import List
import heapq


class UnionFind:
    def __init__(self, num) -> None:
        self.head = list(range(num))
        self.size = [1] * num
        self.setNum = num

    def find(self, index) -> int:
        if self.head[index] != index:
            self.head[index] = self.find(self.head[index])
        return self.head[index]

    def union(self, index1, index2) -> bool:
        x, y = self.find(index1),self.find(index2)
        if x == y :
            return False
        if self.size[x] < self.size[y]:
            x, y = y, x
        self.head[y] = x
        self.size[x] += self.size[y]
        self.setNum -= 1
        return True
    
    def connected(self, x: int, y: int) -> bool:
        return self.find(x) == self.find(y)
        

class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        res = 0
        n = len(grid)
        heap = [(grid[0][0], 0, 0)]
        visited = set([(0, 0)])

        while heap:
            height, x, y = heapq.heappop(heap)
            res = max(res, height)
            if x == n-1 and y == n-1:
                return res

            for dx, dy in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                x1, y1 = x + dx, y + dy
                if 0 <= x1 < n and 0 <= y1 < n and (x1, y1) not in visited:
                    visited.add((x1, y1))
                    heapq.heappush(heap, (grid[x1][y1], x1, y1))

        return -1

    def swimInWater_union_find(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        edges = list()
        for i in range(m):
            for j in range(n):
                iden = i * n + j
                if i > 0:
                    edges.append((iden - n, iden, max(grid[i][j], grid[i-1][j])))
                if j > 0:
                    edges.append((iden - 1, iden, max(grid[i][j], grid[i][j-1])))
        
        edges.sort(key=lambda e: e[2])

        uf = UnionFind(m * n)
        ans = 0
        for x, y, v in edges:
            uf.union(x, y)
            if uf.connected(0, m * n - 1):
                ans = v
                break
        
        return ans
