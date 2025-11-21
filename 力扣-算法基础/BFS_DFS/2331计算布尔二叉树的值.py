from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def evaluateTree(self, root: Optional[TreeNode]) -> bool:
        def dfs(node):
            # 已知题目给的树为完整二叉树
            # 叶子节点
            if node.left is None:
                return node.val
            # 如果是非叶子节点
            left = dfs(node.left)
            right = dfs(node.right)

            if node.val == 2:
                return left or right
            else:
                return left and right

        return bool(dfs(root))
