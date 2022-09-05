'''
用以太网线缆将 n 台计算机连接成一个网络，计算机的编号从 0 到 n-1。线缆用 connections 表示，其中 connections[i] = [a, b] 连接了计算机 a 和 b。
网络中的任何一台计算机都可以通过网络直接或者间接访问同一个网络中其他任意一台计算机。
给你这个计算机网络的初始布线 connections，你可以拔开任意两台直连计算机之间的线缆，并用它连接一对未直连的计算机。请你计算并返回使所有计算机都连通所需的最少操作次数。如果不可能，则返回 -1 。 

策略：找连通分量，所以先考虑的并查集；DFS同样可以
'''
from typing import List
import collections

class UnionFind:
    def __init__(self, n) -> None:
        super().__init__()
        self.head = list(range(n))
    
    def find(self, index) -> int:
        if self.head[index] != index:
            self.head[index] = self.find(self.head[index])
        return self.head[index]
    
    def union(self, index1, index2):
        self.head[self.find(index2)] = self.find(index1)


class Solution:
    def makeConnected(self, n: int, connections: List[List[int]]) -> int:
        num_edges = len(connections)
        if num_edges < n - 1:
            return -1
        uf = UnionFind(n)
        for connection in connections:
            uf.union(connection[0], connection[1])
        print(uf.head)
        group = collections.defaultdict(lambda :0)
        for node in uf.head:
            group[uf.find(node)] += 1
        return len(group) - 1


class Solution_dfs:
    def makeConnected(self, n: int, connections: List[List[int]]) -> int:
        num_edges = len(connections)
        if num_edges < n - 1:
            return -1
        edges = collections.defaultdict(list)
        for connection in connections:
            edges[connection[0]].append(connection[1])
            edges[connection[1]].append(connection[0])
        seen = set()
        def dfs(node):
            seen.add(node)
            for v in edges[node]:
                if v not in seen:
                    dfs(v)
        ans = 0
        for i in range(n):
            if i not in seen:
                dfs(i)
                ans += 1
        return ans - 1

solution = Solution_dfs()
print(solution.makeConnected(6, [[0,1],[0,2],[0,3],[1,2],[1,3]]))