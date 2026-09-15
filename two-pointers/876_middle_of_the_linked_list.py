from common import ListNode


def middle_node(head: ListNode) -> ListNode:
    fast = slow = head
    while fast and fast.next:
        fast = fast.next.next
        slow = slow.next
    return slow
