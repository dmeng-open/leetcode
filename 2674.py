from typing import List, Optional

from common import ListNode

# O(n) | O(1)
class Solution:
    def split(self, head: Optional[ListNode]) -> List[Optional[ListNode]]:
        x = y = head
        while y.next != head and y.next.next != head:
            x = x.next
            y = y.next.next
        if y.next.next == head:
            y = y.next
        second = x.next
        x.next = head
        y.next = second
        return [head, second]