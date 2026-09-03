from typing import Optional
from common import ListNode

# o - 1 2 3 4 4 4 5 5 5
#         k
#                  i
#                  j
def dedup(head: Optional[ListNode]) -> Optional[ListNode]:
    # if not head:
    #     return None
    # root = ListNode(0, head)
    # k = root
    # i = head
    # j = i.next
    # while j:
    #     while j and i.val == j.val:
    #         j = j.next
    #     if i.next == j: # No dups
    #         k = i
    #         i = j
    #     else:
    #         # k stays because j still needs to be evaluated for dups
    #         k.next = j
    #         i = j # j will move next in the next iteration's while loop
    # return root.next

    root = ListNode(0, head)
    prev = root
    curr = head
    while curr:
        if curr.next and curr.next.val == curr.val:
            dup = curr.val
            while curr and curr.next.val == dup:
                curr = curr.next
            prev.next = curr
            # prev stays because curr needs to be evaluated
        else:
            prev = curr
            curr = curr.next
    return root.next