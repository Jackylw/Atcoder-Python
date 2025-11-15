from typing import Optional, List


class Node:
    def __init__(self, val: Optional[int] = None, children: Optional[List['Node']] = None):
        self.val = val
        self.children = children


class Solution:
    # 队列法
    def levelOrder(self, root: 'Node') -> List[List[int]]:
        if root is None:
            return []

        res = []
        # 队列，用于存储每一层的节点
        queue = [root]
        while queue:
            level = []  # 存储当前层的节点值
            for i in range(len(queue)):
                node = queue.pop(0)
                level.append(node.val)
                if node.children:
                    queue.extend(node.children)
            res.append(level)

        return res


print(Solution().levelOrder(Node(1, [Node(3, [Node(5), Node(6)]), Node(2), Node(4)])))
