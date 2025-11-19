from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head

        dummy = ListNode(0)
        dummy.next = head
        pre = dummy

        while pre.next and pre.next.next:
            first = pre.next
            second = pre.next.next
            
            # 交换
            pre.next = second
            first.next = second.next
            second.next = first
            
            pre = first
            
        return dummy.next