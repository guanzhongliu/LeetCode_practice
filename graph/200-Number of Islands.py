'''
Given an m x n 2D binary grid grid which represents a map of '1's (land) and '0's (water), 
return the number of islands.

An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically. 
You may assume all four edges of the grid are all surrounded by water.

Example:
Input: grid = [
  ["1","1","1","1","0"],
  ["1","1","0","1","0"],
  ["1","1","0","0","0"],
  ["0","0","0","0","0"]
]
Output: 1

'''
# 用并查集，似乎没有DFS和BFS快

class UnionFind:
    def __init__(self, n) -> None:
        super().__init__()
        self.head = list(range(n))

    def find(self, index) -> int:
        if (self.head[index] != index):
            self.head[index] = self.find(self.head[index])
        return self.head[index]

    def union(self, idx1, idx2) -> int:
        self.head[self.find(idx2)] = self.find(idx1)


class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        m = len(grid)
        n = len(grid[0])
        uf = UnionFind(m * n)
        for i in range(m):
            for j in range(n):
                idx = i * n + j
                if grid[i][j] == '0':
                    uf.head[idx] = -1
                else:
                    if i - 1 >= 0 and grid[i - 1][j] == '1':
                        uf.union(idx, idx - n)
                    if j - 1 >= 0 and grid[i][j -1 ] == '1':
                        uf.union(idx, idx - 1)
        ans = set()
        for i in uf.head:
            if i != -1:
                # 最后head的保存的坐标可能不统一
                ans.add(uf.find(i))
        return len(ans)
