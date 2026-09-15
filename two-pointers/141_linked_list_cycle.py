from typing import Optional

from common import ListNode


def has_cycle(head: Optional[ListNode]) -> bool:
    fast = slow = head
    while fast and fast.next:
        fast = fast.next.next
        slow = slow.next
        if fast == slow:
            return True
    return False
