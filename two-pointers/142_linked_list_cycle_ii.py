from typing import Optional

from common import ListNode

# O(n) | O(1)
def detect_cycle(head: Optional[ListNode]) -> Optional[ListNode]:
    slow = fast = head
    while fast and fast.next:
        fast = fast.next.next
        slow = slow.next
        if slow == fast:
            slow = head
            while slow != fast:
                slow = slow.next
                fast = fast.next
            return slow
    return None
