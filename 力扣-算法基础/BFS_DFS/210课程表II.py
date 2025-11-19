from typing import List
from collections import deque


class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        # 建图：邻接表 & 入度数组
        adj = [[] for _ in range(numCourses)]
        indegree = [0] * numCourses
        for cur, pre in prerequisites:
            adj[pre].append(cur)
            indegree[cur] += 1

        # 将所有入度为 0 的节点入队
        q = deque([i for i in range(numCourses) if indegree[i] == 0])
        order = []

        while q:
            node = q.popleft()
            order.append(node)
            for neighbor in adj[node]:
                indegree[neighbor] -= 1
                if indegree[neighbor] == 0:
                    q.append(neighbor)

        # 若所有课程都能排完，则 order 长度为 numCourses；否则有环
        return order if len(order) == numCourses else []
