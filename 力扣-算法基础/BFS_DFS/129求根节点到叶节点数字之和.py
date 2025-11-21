from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        ans = 0

        def dfs(node, x):
            if node is None:
                return
            x = x * 10 + node.val
            if node.left is None and node.right is None:
                nonlocal ans
                ans += x
                return
            dfs(node.left, x)
            dfs(node.right, x)

        dfs(root, 0)
        return ans
