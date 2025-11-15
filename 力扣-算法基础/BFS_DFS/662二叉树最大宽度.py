from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0

        res = 0
        # 使用元组 (node, position) 来记录节点及其位置
        queue = [(root, 1)]

        while queue:
            # 当前行的最左和最右位置
            left_pos = queue[0][1]
            right_pos = queue[-1][1]

            # 更新最大宽度
            res = max(res, right_pos - left_pos + 1)

            # 处理下一层节点
            next_level = []
            for node, pos in queue:
                if node.left:
                    next_level.append((node.left, pos * 2))
                if node.right:
                    next_level.append((node.right, pos * 2 + 1))

            queue = next_level

        return res


print(Solution().widthOfBinaryTree(TreeNode(1, TreeNode(3, TreeNode(5), TreeNode(3)), TreeNode(2, None, TreeNode(9)))))


class Solution1:
    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0

        res = 0
        queue = [(root, 1)]
        while queue:
            level = []
            left = queue[0][1]
            right = queue[-1][1]
            res = max(res, right - left + 1)
            for i in range(len(queue)):
                # 处理下一层
                if queue[i][0].left:
                    level.append((queue[i][0].left, queue[i][1] * 2))
                if queue[i][0].right:
                    level.append((queue[i][0].right, queue[i][1] * 2 + 1))
            queue = level
        return res


print(Solution1().widthOfBinaryTree(TreeNode(1, TreeNode(3, TreeNode(5), TreeNode(3)), TreeNode(2, None, TreeNode(9)))))
