'''
You are given an array of k linked-lists lists, 
each linked-list is sorted in ascending order.

Merge all the linked-lists into one sorted linked-list and return it.

Example 1:
Input: lists = [[1,4,5],[1,3,4],[2,6]]
Output: [1,1,2,3,4,4,5,6]
Explanation: The linked-lists are:
[
  1->4->5,
  1->3->4,
  2->6
]
merging them into one sorted list:
1->1->2->3->4->4->5->6

'''

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

import heapq


class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        # 用一个heapq维护，但这里有一个坑需要注意：tuple在进行比较操作时会逐元素进行比较
        # 而leetcode在实现ListNode时候显然不会实现比较器
        # 因此heapq维护的元素不能有ListNode的实例
        # 改为另存了一个每个list头指针组成的list，然后heapq的第二位保存其索引
        ans = cur = ListNode(0)
        nums = []
        ptr_list = []
        for i in range(len(lists)):
            heapq.heappush(nums, (lists[i].val, i))  # 这里i是把list的索引放进来，方便pop之后把下一个加进来
            ptr_list.append(lists[i])
        while len(nums) != 0:
            val, lid = heapq.heappop(nums)
            cur.next = ListNode(val)
            cur = cur.next
            if ptr_list[lid].next != None:
                ptr_list[lid] = ptr_list[lid].next
                heapq.heappush(nums, (ptr_list[lid].val, lid))
        return ans.next

        