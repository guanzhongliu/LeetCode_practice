'''
给定一个列表 accounts，每个元素 accounts[i] 是一个字符串列表，其中第一个元素 accounts[i][0] 是 名称 (name)，其余元素是 emails 表示该账户的邮箱地址。
现在，我们想合并这些账户。如果两个账户都有一些共同的邮箱地址，则两个账户必定属于同一个人。
请注意，即使两个账户具有相同的名称，它们也可能属于不同的人，因为人们可能具有相同的名称。一个人最初可以拥有任意数量的账户，但其所有账户都具有相同的名称。
合并账户后，按以下格式返回账户：每个账户的第一个元素是名称，其余元素是按顺序排列的邮箱地址。账户本身可以以任意顺序返回。


思路：(1)并查集    (2)构建无向图，DFS
'''

from typing import List
import collections

accounts = [["John", "johnsmith@mail.com", "john00@mail.com"], ["John", "johnnybravo@mail.com"],
            ["John", "johnsmith@mail.com", "john_newyork@mail.com"], ["Mary", "mary@mail.com"]]


class UnionFind():
    def __init__(self, n) -> None:
        super().__init__()
        self.head = list(range(n))
    
    def find(self, index) -> int:
        if(self.head[index] != index):
            self.head[index] = self.find(self.head[index])
        return self.head[index]

    def union(self, index1, index2):
        self.head[self.find(index2)] = self.find(index1)

class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        email2index = {}
        email2name = {}
        for account in accounts:
            for i in account[1:]:
                if i not in email2index:
                    email2index[i] = len(email2index)
                    email2name[i] = account[0]

        uf = UnionFind(len(email2index)) 

        for account in accounts:
            for i in account[2:]:
                uf.union(email2index[account[1]], email2index[i])
        index2emails = collections.defaultdict(list)

        for email, index in email2index.items():
            index2emails[uf.find(index)].append(email)

        ans = list()
        for emails in index2emails.values():
            ans.append([email2name[emails[0]]] + sorted(emails))
        return ans

class Solution_DFS:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        # 构建无向图，每个邮箱为一个节点，同一个账户的邮箱全部相连
        # 有多少连通分量，就有多少独立的账户
        # 该字典，键为一个邮箱，值为与其相连的所有邮箱
        graph = collections.defaultdict(list)
        for account in accounts:
            master = account[1]
            for email in list(set(account[2:])):
                graph[master].append(email)
                graph[email].append(master)

        res = []  # 最终的输出结果
        visited = set()  # 标记集合

        for account in accounts:
            emails = []  # 存储该账户的所有邮箱
            # 深度优先遍历
            self.dfs(account[1], graph, visited, emails)
            if emails:
                res.append([account[0]] + sorted(emails))
        return res

    # 深度优先遍历
    def dfs(self, email, graph, visited, emails):
        # 访问过，不在添加直接结束
        if email in visited:
            return
        visited.add(email)  # 标记访问
        emails.append(email)  # 添加
        for neighbor in graph[email]:
            self.dfs(neighbor, graph, visited, emails)

solution = Solution()
print(solution.accountsMerge(accounts))
