from common import ListNode


def middle(head: ListNode) -> ListNode:
    runner = walker = head
    while runner and runner.next:
        runner = runner.next.next
        walker = walker.next
    return walker