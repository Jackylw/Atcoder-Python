from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        # 定义快慢指针找中点
        slow = fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        # 当 fast.next 为 None 时，slow 节点就是中点
        # 反转后半段链表
        pre = None
        cur = slow
        while cur:
            next = cur.next
            cur.next = pre
            pre = cur
            cur = next

        # 链表合并
        cur1 = head
        cur2 = pre

        while cur2.next:
            next1 = cur1.next
            next2 = cur2.next
            # 连接
            cur1.next = cur2
            cur2.next = next1
            # 移动
            cur1 = next1
            cur2 = next2
