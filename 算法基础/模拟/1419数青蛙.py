class Solution:
    def minNumberOfFrogs(self, croakOfFrogs: str) -> int:
        if len(croakOfFrogs) % 5:
            return -1
        ans , now_num = 0 , 0
        cnt = [0] * 4
        mp = {'c':0, 'r':1, 'o':2, 'a':3, 'k':4}
        for c in croakOfFrogs:
            t = mp[c]
            if t == 0:
                now_num += 1
                cnt[t] += 1

