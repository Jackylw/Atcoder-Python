from collections import deque, defaultdict
from typing import List

class Solution:
    def alienOrder(self, words: List[str]) -> str:
        # 构建图：记录每个节点的后继节点
        graph = defaultdict(set)
        # 记录每个节点的入度
        in_degree = defaultdict(int)
        # 初始化所有出现的字母的入度为0
        for word in words:
            for ch in word:
                in_degree[ch] = 0
        
        # 逐对比较相邻单词，构建有向边
        for i in range(len(words) - 1):
            pre, nxt = words[i], words[i + 1]
            min_len = min(len(pre), len(nxt))
            # 检查是否出现非法情况：前面完全相同但前一个单词更长
            if pre[:min_len] == nxt[:min_len] and len(pre) > len(nxt):
                return ""
            # 找到第一个不同的字符，建立有向边
            for j in range(min_len):
                if pre[j] != nxt[j]:
                    u, v = pre[j], nxt[j]
                    # 避免重复添加同一条边
                    if v not in graph[u]:
                        graph[u].add(v)
                        in_degree[v] += 1
                    break
        
        # 拓扑排序（BFS）
        queue = deque([ch for ch in in_degree if in_degree[ch] == 0])
        order = []
        while queue:
            u = queue.popleft()
            order.append(u)
            for v in graph[u]:
                in_degree[v] -= 1
                if in_degree[v] == 0:
                    queue.append(v)
        
        # 如果拓扑排序包含所有字母，则返回结果；否则存在环，返回空串
        if len(order) == len(in_degree):
            return "".join(order)
        else:
            return ""
