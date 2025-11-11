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
        # 处理空链表或只有一个节点的情况
        if not head or not head.next:
            return
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

def build_list(arr):
    """根据数组构造链表，返回头节点"""
    if not arr:
        return None
    head = ListNode(arr[0])
    cur = head
    for val in arr[1:]:
        cur.next = ListNode(val)
        cur = cur.next
    return head


def print_list(head):
    """打印链表"""
    vals = []
    while head:
        vals.append(str(head.val))
        head = head.next
    print(" -> ".join(vals))


if __name__ == "__main__":
    # 测试用例
    test_cases = [
        [1, 2, 3, 4],
        [1, 2, 3, 4, 5],
        [1],
        []
    ]

    for arr in test_cases:
        head = build_list(arr)
        print("原链表：", end="")
        print_list(head)
        Solution().reorderList(head)
        print("重排后：", end="")
        print_list(head)
        print("-" * 30)



