from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if root is None:
            return []

        res = []
        queue = [root]
        left_to_right = True  # 第一层从左到右
        while queue:
            level = []
            for _ in range(len(queue)):
                node = queue.pop(0)
                if left_to_right:
                    level.append(node.val)
                else:
                    level.insert(0, node.val)
                # 记录下一层的节点
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            res.append(level)
            # 切换方向
            left_to_right = not left_to_right
        return res
