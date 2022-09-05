'''
Merge Two Sorted Lists

You are given the heads of two sorted linked lists list1 and list2.

Merge the two lists in a one sorted list. 
The list should be made by splicing together the nodes of the first two lists.

Return the head of the merged linked list.

Example 1:
Input: list1 = [1,2,4], list2 = [1,3,4]
Output: [1,1,2,3,4,4]

Example 2:
Input: list1 = [], list2 = []
Output: []

Example 3:
Input: list1 = [], list2 = [0]
Output: [0]
'''

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def mergeTwoLists(self, list1, list2):
        """
        :type list1: Optional[ListNode]
        :type list2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        # 如果任意一个为空
        if list1 == None:
            return list2
        if list2 == None:
            return list1
        # 决定哪个是开头
        if list1.val < list2.val:
            start = list1
            addition = list2
        else:
            start = list2
            addition = list1
        ans = start
        # 逐个添加
        while start.next and addition:
            # 需要插入
            if addition.val < start.next.val:
                start.next, tmp, addition = addition, start.next, addition.next
                start.next.next = tmp
                start = start.next
            # 移到下一个
            else:
                start = start.next
        # 没有插入完
        if addition:
            start.next = addition
        return ans
            