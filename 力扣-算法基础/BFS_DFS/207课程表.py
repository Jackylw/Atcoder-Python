from collections import deque
from typing import List


class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adj = [[] for _ in range(numCourses)]
        indegree = [0] * numCourses
        for cur, pre in prerequisites:
            adj[pre].append(cur)
            indegree[cur] += 1
        
        # 将所有入度为 0 的节点入队
        q = deque([i for i in range(numCourses) if indegree[i] == 0])
        learned = 0  # 已学习课程数

        while q:
            pre = q.popleft()
            learned += 1
            for cur in adj[pre]:
                indegree[cur] -= 1
                if indegree[cur] == 0:
                    q.append(cur)

        # 若所有课程都能学完，则 learned 等于 numCourses
        return learned == numCourses