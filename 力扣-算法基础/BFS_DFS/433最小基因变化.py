from typing import List
from collections import deque


class Solution:
    def minMutation(self, startGene: str, endGene: str, bank: List[str]) -> int:
        if startGene == endGene:
            return 0
            
        bank_set = set(bank)
        if endGene not in bank_set:
            return -1
            
        # BFS队列：(当前基因, 变化次数)
        queue = deque([(startGene, 0)])
        
        while queue:
            current, steps = queue.popleft()
            
            # 遍历当前基因的每个字符位置
            for i in range(len(current)):
                # 尝试将当前位置的字符替换为其他可能的基因字符
                for gene in "ACGT":
                    if current[i] == gene:
                        continue
                        
                    # 生成新的基因序列
                    new_gene = current[:i] + gene + current[i+1:]
                    
                    # 检查新基因是否在bank中
                    if new_gene in bank_set:
                        if new_gene == endGene:
                            return steps + 1
                        # 从bank中移除该基因，表示已访问
                        bank_set.remove(new_gene)
                        # 加入队列，继续搜索
                        queue.append((new_gene, steps + 1))
        
        # 如果无法通过bank中的序列到达目标基因，返回-1
        return -1


# 测试用例
if __name__ == "__main__":
    solution = Solution()
    
    # 测试用例1
    start1 = "AACCGGTT"
    end1 = "AACCGGTA"
    bank1 = ["AACCGGTA"]
    print("测试用例1:")
    print(f"start: {start1}, end: {end1}, bank: {bank1}")
    print(f"结果: {solution.minMutation(start1, end1, bank1)}")  # 预期输出: 1
    
    # 测试用例2
    start2 = "AACCGGTT"
    end2 = "AAACGGTA"
    bank2 = ["AACCGGTA", "AACCGCTA", "AAACGGTA"]
    print("\n测试用例2:")
    print(f"start: {start2}, end: {end2}, bank: {bank2}")
    print(f"结果: {solution.minMutation(start2, end2, bank2)}")  # 预期输出: 2
    
    # 测试用例3
    start3 = "AAAAACCC"
    end3 = "AACCCCCC"
    bank3 = ["AAAACCCC", "AAACCCCC", "AACCCCCC"]
    print("\n测试用例3:")
    print(f"start: {start3}, end: {end3}, bank: {bank3}")
    print(f"结果: {solution.minMutation(start3, end3, bank3)}")  # 预期输出: 3
        
        