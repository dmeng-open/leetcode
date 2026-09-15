from typing import Optional
from common import ListNode

# o - 1 2 3 4 4 4 5 5 5
#         prev
#                  curr
#                  (scan ahead for dups)
def delete_duplicates(head: Optional[ListNode]) -> Optional[ListNode]:
    # if not head:
    #     return None
    # root = ListNode(0, head)
    # prev = root
    # curr = head
    # ahead = curr.next
    # while ahead:
    #     while ahead and curr.val == ahead.val:
    #         ahead = ahead.next
    #     if curr.next == ahead: # No dups
    #         prev = curr
    #         curr = ahead
    #     else:
    #         # prev stays because ahead still needs to be evaluated for dups
    #         prev.next = ahead
    #         curr = ahead # ahead will move next in the next iteration's while loop
    # return root.next

    root = ListNode(0, head)
    prev = root
    curr = head
    while curr:
        if curr.next and curr.next.val == curr.val:
            dup = curr.val
            while curr.next and curr.next.val == dup:
                curr = curr.next
            curr = curr.next
            prev.next = curr
            # prev stays because curr needs to be evaluated
        else:
            prev = curr
            curr = curr.next
    return root.next
