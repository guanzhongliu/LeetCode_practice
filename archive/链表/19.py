'''
给你一个链表，删除链表的倒数第 n 个结点，并且返回链表的头结点。
'''


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        node1 = s = ListNode(next=head)
        node2 = head
        for i in range(n):
            node2 = node2.next
        while node2:
            node2 = node2.next
            node1 = node1.next
        
        node1.next = node1.next.next
        return s.next