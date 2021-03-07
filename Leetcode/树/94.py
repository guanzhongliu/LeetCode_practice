'''
给定一个二叉树的根节点 root ，返回它的 中序 遍历。
'''
from typing import List

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def inOrder(self, root: TreeNode, res: List):
        if not root:
            return
        self.inOrder(root.left, res)
        res.append(root.val)
        self.inOrder(root.right, res)

    def inorderTraversal(self, root: TreeNode) -> List[int]:
        res = []
        self.inOrder(root, res)

        return res