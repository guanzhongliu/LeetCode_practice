'''
You are given two non-empty linked lists representing two non-negative integers. 
The digits are stored in reverse order, and each of their nodes contains a single digit. 
Add the two numbers and return the sum as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.

Example:
Input: l1 = [2,4,3], l2 = [5,6,4]
Output: [7,0,8]
Explanation: 342 + 465 = 807.
'''
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        # 模拟即可，但我的方法有些麻烦
        add_on = 0
        ans = ListNode()
        cur = ans
        while l1 != None and l2 != None:
            n = l1.val + l2.val + add_on
            tmp = ListNode(n % 10)
            cur.next = tmp
            add_on = n // 10
            l1, l2, cur = l1.next, l2.next, cur.next
        if not l1:
            while (l2):
                n = l2.val + add_on
                tmp = ListNode(n % 10)
                cur.next = tmp
                add_on = n // 10
                l2, cur = l2.next, cur.next
        else:
            while (l1):
                n = l1.val + add_on
                tmp = ListNode(n % 10)
                cur.next = tmp
                add_on = n // 10
                l1, cur = l1.next, cur.next
        if add_on:
            cur.next = ListNode(add_on)
        return ans.next
    
    def sample_answer(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummyHead = ListNode(0)
        curr = dummyHead
        carry = 0
        # 其实可以写进一个循环呜呜呜
        while l1 != None or l2 != None or carry != 0:
            l1Val = l1.val if l1 else 0
            l2Val = l2.val if l2 else 0
            columnSum = l1Val + l2Val + carry
            carry = columnSum // 10
            newNode = ListNode(columnSum % 10)
            curr.next = newNode
            curr = newNode
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None
        return dummyHead.next
        