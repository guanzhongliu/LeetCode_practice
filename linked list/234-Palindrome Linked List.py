'''
Given the head of a singly linked list, return true if it is a palindrome or false otherwise.

Example 1:
Input: head = [1,2,2,1]
Output: true

Example 2:
Input: head = [1,2]
Output: false

'''

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        # 1. 把值保存下来，再双指针
        nums = []
        while head:
            nums.append(head.val)
            head = head.next
        start = 0
        end = len(nums) - 1
        while start < end:
            if nums[start] != nums[end]:
                return False
            start += 1
            end -= 1
        # 2.另一个空间O(1)的解法是，把后半段链表反转一下...
        return True
        
        
            
        