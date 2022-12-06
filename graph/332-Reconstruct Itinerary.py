'''
You are given a list of airline tickets where tickets[i] = [fromi, toi] represent the departure and the arrival airports of one flight. Reconstruct the itinerary in order and return it.

All of the tickets belong to a man who departs from "JFK", thus, the itinerary must begin with "JFK". If there are multiple valid itineraries, you should return the itinerary that has the smallest lexical order when read as a single string.

For example, the itinerary ["JFK", "LGA"] has a smaller lexical order than ["JFK", "LGB"].
You may assume all tickets form at least one valid itinerary. You must use all the tickets once and only once.

Example 1:
Input: tickets = [["JFK","SFO"],["JFK","ATL"],["SFO","ATL"],["ATL","JFK"],["ATL","SFO"]]
Output: ["JFK","ATL","JFK","SFO","ATL","SFO"]
Explanation: Another possible reconstruction is ["JFK","SFO","ATL","JFK","ATL","SFO"] but it is larger in lexical order.

'''

from collections import defaultdict
class Solution(object):
    def findItinerary(self, tickets):
        """
        :type tickets: List[List[str]]
        :rtype: List[str]
        """
        num = 1
        # 用字典存储每个城市的下一个城市列表
        ticket_dict = defaultdict(list)
        for ticket in tickets:
            ticket_dict[ticket[0]].append(ticket[1])
            num += 1
        # 按字母顺序排序,这里用降序是因为pop()是从后面取出元素
        for k in ticket_dict.keys():
            ticket_dict[k].sort(reverse=True)
        self.route = []
        self.DFS('JFK', ticket_dict)
        return self.route[::-1]

    # 这里的思路是从起点开始, 每次都取下一个城市, 如果下一个城市没有下一个城市了, 就把这个城市加入到结果中
    # 如果下一个城市还有下一个城市, 就继续递归, 直到没有下一个城市了, 就把这个城市加入到结果中
    # 因为问题保证了有解, 所以这里不会出现死循环
    def DFS(self, city, ticket_dict):
        nxt_lists = ticket_dict[city]
        
        while nxt_lists:
            self.DFS(nxt_lists.pop(), ticket_dict)
        
        self.route.append(city)

