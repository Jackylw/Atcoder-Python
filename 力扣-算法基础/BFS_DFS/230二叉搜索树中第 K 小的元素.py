# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    # 中序递归法
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        res = []

        def inorder(root):
            if not root:
                return
            inorder(root.left)  # 左
            res.append(root.val)  # 中
            inorder(root.right)  # 右

        inorder(root)
        return res[k - 1]

    # 迭代法
    def kthSmallest2(self, root: Optional[TreeNode], k: int) -> int:
        stack = []
        while root or stack:
            # 一路走到最左边
            while root:
                stack.append(root)
                root = root.left
            # 处理最左边
            root = stack.pop()
            k -= 1
            if k == 0:
                return root.val
            root = root.right
