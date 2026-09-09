from typing import Optional

from common import ListNode

# Time: O(n)
# Space: O(1)
def remove_nth_from_end(head: Optional[ListNode], n: int) -> Optional[ListNode]:
    root = ListNode(0, head)
    i = j = root

    for _ in range(n):
        j = j.next
   
    while j.next:
        i = i.next
        j = j.next

    i.next = i.next.next

    return root.next
