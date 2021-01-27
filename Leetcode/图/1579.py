'''
Alice 和 Bob 共有一个无向图，其中包含 n 个节点和 3  种类型的边：

类型 1：只能由 Alice 遍历。
类型 2：只能由 Bob 遍历。
类型 3：Alice 和 Bob 都可以遍历。
给你一个数组 edges ，其中 edges[i] = [typei, ui, vi] 表示节点 ui 和 vi 之间存在类型为 typei 的双向边。请你在保证图仍能够被 Alice和 Bob 完全遍历的前提下，找出可以删除的最大边数。如果从任何节点开始，Alice 和 Bob 都可以到达所有其他节点，则认为图是可以完全遍历的。

返回可以删除的最大边数，如果 Alice 和 Bob 无法完全遍历图，则返回 -1 。

策略：贪心 + 并查集
'''
import collections
from typing import List


class UnionFind:
    def __init__(self, num) -> None:
        self.head = [list(range(num)), list(range(num))]
        self.ans = 0
    
    def find(self, t, index) -> int:
        if self.head[t][index] != index:
            self.head[t][index] = self.find(t, self.head[t][index])
        return self.head[t][index]
    
    def union(self, t, index1, index2):
        if self.find(t, index1) == self.find(t, index2):
            self.ans += 1
            return False
        self.head[t][self.find(t, index2)] = self.find(t, self.head[t][index1])
        return True
class Solution:
    
    def maxNumEdgesToRemove(self, n: int, edges: List[List[int]]) -> int:
        uf = UnionFind(n)
        edges.sort(key=lambda x:x[0], reverse=True)
        for edge in edges:
            if edge[0] == 3:
                flag = uf.union(0, edge[1]-1, edge[2]-1)
                if flag:
                    uf.union(1, edge[1]-1, edge[2]-1)
            else:
                uf.union(edge[0]-1, edge[1]-1, edge[2]-1)
        g = 0
        for i in range(2):
            group = collections.defaultdict(lambda :0)
            for h in uf.head[i]:
                group[uf.find(i, h)] += 1
            g += len(group)
        if g == 2:
            return uf.ans
        return -1

solution = Solution()
n = 4
edges =  [[3,1,2], [3,3,4], [1,1,3],[2,2,4]]
print(solution.maxNumEdgesToRemove(n, edges))