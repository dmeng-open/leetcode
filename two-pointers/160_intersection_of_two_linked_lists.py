from typing import Optional
from common import ListNode

# T: O(n + m)
# S: O(1)
def get_intersection_node(a: ListNode, b: ListNode) -> Optional[ListNode]: 
    a_ptr, b_ptr = a, b
    while a_ptr != b_ptr:
        a_ptr = a_ptr.next if a_ptr else b
        b_ptr = b_ptr.next if b_ptr else a
    return a_ptr
