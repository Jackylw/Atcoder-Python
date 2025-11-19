from typing import List

class Solution:
    def hanota(self, A: List[int], B: List[int], C: List[int]) -> None:
        def _move_disks(n: int, source: List[int], auxiliary: List[int], destination: List[int]):
            if n == 0:
                return
            # 将 n-1 个盘子从 source 移动到 auxiliary，以 destination 为临时柱子
            _move_disks(n - 1, source, destination, auxiliary)
            # 将第 n 个盘子从 source 移动到 destination
            destination.append(source.pop())
            # 将 n-1 个盘子从 auxiliary 移动到 destination，以 source 为临时柱子
            _move_disks(n - 1, auxiliary, source, destination)

        _move_disks(len(A), A, B, C)


A_test = [1, 2, 3]
B_test = []
C_test = []
Solution().hanota(A_test, B_test, C_test)
print(C_test)
