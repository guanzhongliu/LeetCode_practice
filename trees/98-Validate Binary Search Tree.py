'''
Given the root of a binary tree, determine if it is a valid binary search tree (BST).

A valid BST is defined as follows:

The left subtree of a node contains only nodes with keys less than the node's key.
The right subtree of a node contains only nodes with keys greater than the node's key.
Both the left and right subtrees must also be binary search trees.

Example 1:
Input: root = [2,1,3]
Output: true

Example 2:
Input: root = [5,1,4,null,null,3,6]
Output: false
Explanation: The root node's value is 5 but its right child's value is 4.
'''

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        # 不是简单递归
        # 需要保证左子树的最大值小于根节点，右子树的最小值大于根节点

        def is_valid(node, min_val, max_val):
            if not node.left and not node.right:
                return node.val > min_val and node.val < max_val
            elif not node.left:
                ans = node.val < node.right.val and node.val > min_val and node.val < max_val
                return ans and is_valid(node.right, node.val, max_val)
            elif not node.right:
                ans = node.val > node.left.val and node.val > min_val and node.val < max_val
                return ans and is_valid(node.left, min_val, node.val)
            else:
                ans = node.val > node.left.val and node.val < node.right.val and node.val > min_val and node.val < max_val
                return ans and is_valid(node.left, min_val, node.val) and is_valid(node.right, node.val, max_val)

        return is_valid(root, -float('inf'), float('inf'))

