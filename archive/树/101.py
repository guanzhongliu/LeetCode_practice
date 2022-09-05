'''
给定一个二叉树，检查它是否是镜像对称的。
'''

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def check(self, n1: TreeNode, n2: TreeNode) -> bool:
        if not n1 and not n2:
            return True
        elif not n1 or not n2:
            return False
        else:
            return n1.val == n2.val and self.check(n1.left, n2.right) and self.check(n1.right, n2.left)

    
    def isSymmetric(self, root: TreeNode) -> bool:
        return self.check(root.left, root.right)