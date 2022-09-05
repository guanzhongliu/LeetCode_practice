'''
给你一个链表的头节点 head，请你编写代码，反复删去链表中由 总和 值为 0 的连续节点组成的序列，直到不存在这样的序列为止。
删除完毕后，请你返回最终结果链表的头节点。
你可以返回任何满足题目要求的答案。

（注意，下面示例中的所有序列，都是对 ListNode 对象序列化的表示。）

策略: 前缀和 + 哈希 + 双向队列（栈）， 策略就是利用前缀和遍历，为0则清空栈，出现出现过的数字则弹出至该数字
'''
from collections import deque
import copy

# Definition for singly-linked list.


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def removeZeroSumSublists(self, head: ListNode) -> ListNode:
        temp = 0
        pre_sum = deque()
        sum_dict = set()
        while head is not None:
            temp = temp + head.val
            if temp == 0:
                pre_sum.clear()
                sum_dict.clear()
            elif temp != 0 and temp in sum_dict:
                while pre_sum[-1] != temp:
                    sum_dict.remove(pre_sum.pop())
                sum_dict.remove(pre_sum.pop())     
            else:
                pre_sum.append(temp)
                sum_dict.add(temp)
            head = head.next
        ans = None
        for i in range(len(pre_sum) - 1, -1, -1):
            if i > 0:
                temp = ListNode(pre_sum[i] - pre_sum[i-1])
                temp.next = copy.deepcopy(ans)
                ans = copy.deepcopy(temp)
            else:
                temp = ListNode(pre_sum[i])
                temp.next = copy.deepcopy(ans)
                ans = copy.deepcopy(temp)
        return ans

