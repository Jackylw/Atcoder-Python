class Solution:
    def isUnique(self, astr: str) -> bool:
        l = []
        for i in astr:
            if i in l:
                return False
            else:
                l.append(i)
        return True

    def isUnique2(self, astr: str) -> bool:
        return len(astr) == len(set(astr))

    def isUnique3(self, astr: str) -> bool:
        int_hash = 0
        for i in astr:
            val = ord(i) - ord('a')
            if (int_hash & (1 << val)) > 0:
                return False
            int_hash |= (1 << val)
        return True
