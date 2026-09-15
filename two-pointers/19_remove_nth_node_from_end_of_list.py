from typing import Optional

from common import ListNode

# Time: O(n)
# Space: O(1)
def remove_nth_from_end(head: Optional[ListNode], n: int) -> Optional[ListNode]:
    root = ListNode(0, head)
    slow = fast = root

    for _ in range(n):
        fast = fast.next
   
    while fast.next:
        slow = slow.next
        fast = fast.next

    slow.next = slow.next.next

    return root.next
