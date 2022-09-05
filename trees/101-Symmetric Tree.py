'''
Symmetric Tree

Given the root of a binary tree, 
check whether it is a mirror of itself (i.e., symmetric around its center).

Example 1:
Input: root = [1,2,2,3,4,4,3]
Output: true

Example 2:
Input: root = [1,2,2,null,3,null,3]
Output: false
'''

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        # 递归
        # 两个子树的左右子树是否对称
        # 两个子树的左子树是否对称
        # 两个子树的右子树是否对称
        def isMirror(left, right):
            if not left and not right:
                return True
            elif not left or not right:
                return False
            else:
                return left.val == right.val and isMirror(left.left, right.right) and isMirror(left.right, right.left)
        
        return isMirror(root.left, root.right)