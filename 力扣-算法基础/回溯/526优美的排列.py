from collections import defaultdict


class Solution:
    def countArrangement(self, n: int) -> int:
        ans = 0
        path = []
        used = [False] * (n + 1)

        def f(i, perm):
            if perm % i == 0 or i % perm == 0:
                return True
            return False

        def backtrack():
            nonlocal ans
            if len(path) == n:
                ans += 1
                return

            for i in range(1, n + 1):
                if used[i]:
                    continue
                if f(i, len(path) + 1):
                    used[i] = True
                    path.append(i)
                    backtrack()
                    path.pop()
                    used[i] = False
                else:
                    continue

        backtrack()
        return ans

    def countArrangement2(self, n: int) -> int:
        used = [False] * (n + 1)

        def backtrack(pos):
            if pos > n:
                return 1
            count = 0
            for num in range(1, n + 1):
                if not used[num]:
                    if num % pos == 0 or pos % num == 0:
                        used[num] = True
                        count += backtrack(pos + 1)
                        used[num] = False
            return count

        return backtrack(1)

    def countArrangement3(self, n: int) -> int:
        # 每个位置 i 可以存放哪些数字
        macth = defaultdict(list)
        for i in range(1, n + 1):
            for j in range(1, n + 1):
                if i % j == 0 or j % i == 0:
                    macth[i].append(j)

        ans = 0
        visited = set()

        def backtrack(index):
            if index == n + 1:
                nonlocal ans
                ans += 1
                return

            for num in macth[index]:
                if num not in visited:
                    visited.add(num)
                    backtrack(index + 1)
                    visited.discard(num)

        backtrack(1)
        return ans


print(Solution().countArrangement(2))
print(Solution().countArrangement(1))
