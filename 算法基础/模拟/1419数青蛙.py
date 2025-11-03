class Solution:
    def minNumberOfFrogs(self, croakOfFrogs: str) -> int:
        # 检查长度是否为5的倍数
        if len(croakOfFrogs) % 5:
            return -1

        # 记录处于各个状态的青蛙数量
        cnt = [0, 0, 0, 0, 0]  # 分别对应 c, r, o, a, k 五个状态
        frogs = 0  # 当前正在鸣叫的青蛙数
        max_frogs = 0  # 同时鸣叫的最多青蛙数

        # 字符到状态索引的映射
        mapping = {'c': 0, 'r': 1, 'o': 2, 'a': 3, 'k': 4}

        for char in croakOfFrogs:
            idx = mapping[char]

            if idx == 0:  # 'c' - 开始鸣叫
                cnt[idx] += 1
                frogs += 1
                max_frogs = max(max_frogs, frogs)
            else:
                # 检查前一个状态是否有青蛙可以转移到当前状态
                if cnt[idx - 1] <= 0:
                    return -1  # 无效序列

                cnt[idx - 1] -= 1  # 前一个状态青蛙数减1
                if idx == 4:  # 'k' - 结束鸣叫
                    frogs -= 1
                else:  # 其他中间状态
                    cnt[idx] += 1

        # 检查是否所有青蛙都已完成鸣叫
        if frogs != 0:
            return -1

        return max_frogs
