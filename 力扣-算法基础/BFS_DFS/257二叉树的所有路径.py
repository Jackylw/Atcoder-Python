from typing import Optional, List


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        # DFS
        def dfs(node, path):
            if node:
                path += str(node.val)
                # 如果递归到叶子节点，就将结果存入列表中
                if not node.left and not node.right:
                    paths.append(path)
                else:
                    path += '->'
                    dfs(node.left, path)
                    dfs(node.right, path)

        paths = []
        dfs(root, '')
        return paths

print(Solution().binaryTreePaths(TreeNode(1, TreeNode(2, TreeNode(4), TreeNode(5)), TreeNode(3))))