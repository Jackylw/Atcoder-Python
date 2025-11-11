from typing import List

class Solution:
    def mergeSort(self, record, tmp, l, r):
        if l >= r:
            return 0

        mid = (l + r) // 2
        inv_count = self.mergeSort(record, tmp, l, mid) + self.mergeSort(record, tmp, mid + 1, r)
        i, j, pos = l, mid + 1, l
        while i <= mid and j <= r:
            if record[i] <= record[j]:
                tmp[pos] = record[i]
                i += 1
                inv_count += (j - (mid + 1))
            else:
                tmp[pos] = record[j]
                j += 1
            pos += 1
        for k in range(i, mid + 1):
            tmp[pos] = record[k]
            inv_count += (j - (mid + 1))
            pos += 1
        for k in range(j, r + 1):
            tmp[pos] = record[k]
            pos += 1
        record[l:r+1] = tmp[l:r+1]
        return inv_count

    def reversePairs(self, record: List[int]) -> int:
        n = len(record)
        tmp = [0] * n
        return self.mergeSort(record, tmp, 0, n - 1)