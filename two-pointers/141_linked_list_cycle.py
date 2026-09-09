from typing import Optional

from common import ListNode


def has_cycle(head: Optional[ListNode]) -> bool:
    runner = walker = head
    while runner and runner.next:
        runner = runner.next.next
        walker = walker.next
        if runner == walker:
            return True
    return False