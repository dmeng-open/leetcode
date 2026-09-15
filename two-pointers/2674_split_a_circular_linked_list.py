from typing import List, Optional

from common import ListNode

# O(n) | O(1)
def split_circular_linked_list(head: Optional[ListNode]) -> List[Optional[ListNode]]:
    slow = fast = head
    while fast.next != head and fast.next.next != head:
        slow = slow.next
        fast = fast.next.next
    if fast.next.next == head:
        fast = fast.next
    second = slow.next
    slow.next = head
    fast.next = second
    return [head, second]
