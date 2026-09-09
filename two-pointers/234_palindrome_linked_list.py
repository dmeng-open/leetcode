from typing import Optional

from common import ListNode


class Solution:
    # 1 2 3 2 1
    #         f
    #     s
    # 1 2 2 1
    #         f
    #     s
    def is_palindrome(self, head: Optional[ListNode]) -> bool:
        def reverse(head: ListNode) -> ListNode:
            if not head or not head.next:
                return head
            result = reverse(head.next)
            head.next.next = head
            head.next = None
            return result
        fast = slow = head
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
        slow = reverse(slow)
        fast = head
        while fast and slow:
            if fast.val != slow.val:
                return False
            fast = fast.next
            slow = slow.next
        return True