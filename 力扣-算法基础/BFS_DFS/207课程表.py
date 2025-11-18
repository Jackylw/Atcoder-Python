from collections import deque, defaultdict
from typing import List


class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # 1. 构建图和入度数组
        graph = defaultdict(list)
        indegree = [0] * numCourses

        for course, prereq in prerequisites:
            graph[prereq].append(course)  # prereq -> course
            indegree[course] += 1 # 课程的入度，即该课程的先修课程数

        # 2. 初始化队列：所有入度为 0 的课程
        queue = deque([i for i in range(numCourses) if indegree[i] == 0])
        learned = 0  # 已学习课程数

        # 3. BFS 拓扑排序
        while queue:
            curr = queue.popleft()
            learned += 1
            for neighbor in graph[curr]:
                indegree[neighbor] -= 1
                if indegree[neighbor] == 0:
                    queue.append(neighbor)

        # 4. 判断是否学完所有课程
        return learned == numCourses
