from typing import Optional
from typing import List


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    # 合并排序法
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        dummy = ListNode()
        cur = dummy
        tmp = []
        for i in range(len(lists)):
            while lists[i]:
                tmp.append(lists[i].val)
                lists[i] = lists[i].next

        tmp.sort()
        for i in range(len(tmp)):
            cur.next = ListNode(tmp[i])
            cur = cur.next

        return dummy.next

    # 原地合并
    def mergeKLists2(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        dummy = ListNode()
        cur = dummy
        while lists:
            min_idx = -1
            min_val = float('inf')
            for i in range(len(lists)):
                if lists[i] and lists[i].val < min_val:
                    min_idx = i
                    min_val = lists[i].val
            if min_idx == -1:
                break
            cur.next = lists[min_idx]
            cur = cur.next
            lists[min_idx] = lists[min_idx].next
        return dummy.next
