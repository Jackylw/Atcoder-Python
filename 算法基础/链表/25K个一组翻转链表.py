# Definition for singly-linked list.
from typing import Optional
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        dummy = ListNode(0)
        dummy.next = head
        pre = dummy

        while True:
            tail = pre
            for _ in range(k):
                tail = tail.next
                if not tail:
                    return dummy.next
            
            # 翻转子链表
            # 翻转子链表
            next_group = tail.next  # 保存下一组的头节点
            head_node = pre.next    # 当前组的头节点
            # 翻转当前组
            prev = None
            curr = head_node
            for _ in range(k):
                nxt = curr.next
                curr.next = prev
                prev = curr
                curr = nxt
            # 连接翻转后的子链表
            pre.next = tail         # pre 指向翻转后的头节点（原 tail）
            head_node.next = next_group  # 翻转后的尾节点（原 head）指向下一组
            # 移动 pre 到下一组的前驱
            pre = head_node

    def print_list(self, head:Optional[ListNode]):
        while head:
            print(head.val, end=" -> ")
            head = head.next
        print("None")

Solution().print_list(Solution().reverseKGroup(ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5))))), 2))
Solution().print_list(Solution().reverseKGroup(ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5))))), 3))

