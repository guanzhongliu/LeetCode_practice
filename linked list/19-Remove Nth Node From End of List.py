'''
Given the head of a linked list, remove the nth node from the end of the list and return its head.

Example 1:
Input: head = [1,2,3,4,5], n = 2
Output: [1,2,3,5]

Example 2:
Input: head = [1], n = 1
Output: []

Example 3:
Input: head = [1,2], n = 1
Output: [1]
'''


# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """

        '''
        更快的方法
        prev = ListNode(0, head)
        p1 = prev
        p2 = prev
        
        while n != 0:       # 先将p2移动n位
            p2 = p2.next
            n -= 1
        
        while p2.next:    # 当p2移动到结尾, p1刚好是要删除的前一个节点
            p1 = p1.next
            p2 = p2.next
            
        p1.next = p1.next.next    # 删除p1的下一个即可
        
        return prev.next
        '''

        # 先获取长度，在直接删除
        cur = head
        l = 0
        while cur:
            cur = cur.next
            l += 1
        l = l - n - 1
        cur = head
        if l < 0:
            return head.next
        while l:
            cur = cur.next
            l -= 1

        cur.next = cur.next.next

        return head
