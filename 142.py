from typing import Optional

from common import ListNode

# O(n) | O(1)
class Solution:
    def cycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        x = y = head
        while y and y.next:
            y = y.next.next
            x = x.next
            if x == y:
                x = head
                while x != y:
                    x = x.next
                    y = y.next
                return x
        return None