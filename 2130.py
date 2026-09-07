from typing import Optional

from common import ListNode


class Solution:    
    def pairSum(self, head: Optional[ListNode]) -> int:
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
        # 5 -> 4 -> 2
        # 1 -> 2 ->
        result = 0
        while slow:
            result = max(result, fast.val + slow.val)
            fast = fast.next
            slow = slow.next
        return result