class Solution:
    def wardrobeFinishing(self, m: int, n: int, cnt: int) -> int:
        def num_sum(num):
            total = 0
            while num > 0:
                total += num % 10
                num //= 10
            return total

        visited = [[False] * n for _ in range(m)]
        def dfs(x, y):
            if x < 0 or x >= m or y < 0 or y >= n or visited[x][y]:
                return 0
            if num_sum(x) + num_sum(y) > cnt:
                return 0
            visited[x][y] = True
            return 1 + dfs(x + 1, y) + dfs(x, y + 1)

        return dfs(0, 0)
print(Solution().wardrobeFinishing(4,7,5))