'''
给你两个 非空 的链表，表示两个非负的整数。它们每位数字都是按照 逆序 的方式存储的，并且每个节点只能存储 一位 数字。
请你将两个数相加，并以相同形式返回一个表示和的链表。
你可以假设除了数字 0 之外，这两个数都不会以 0 开头。

策略：链表模拟加法
'''

# Definition for singly-linked list.


from typing import List


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        carry = 0
        res = []
        ans = 0
        while(l1 != None or l2 != None):
            if l1 != None and l2 != None:
                temp = l1.val + l2.val + carry
                ans = temp % 10
                carry = int(temp/10)
                l1 = l1.next
                l2 = l2.next
            elif l1 == None:
                temp = l2.val + carry
                ans = temp % 10
                carry = int(temp/10)
                l2 = l2.next
            elif l2 == None:
                temp = l1.val + carry
                ans = temp % 10
                carry = int(temp/10)
                l1 = l1.next
            res.insert(0, ans)
            
        if carry !=0:
            res.insert(0, carry)
        ans = ListNode(res[0])
        for i in range(1, len(res)):
            ans = ListNode(res[i], ans)
        return ans

solution = Solution()
print(solution.addTwoNumbers(ListNode(1), ListNode(2)).val)