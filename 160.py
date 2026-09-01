from typing import Optional
from common import ListNode

# T: O(n + m)
# S: O(1)
class Solution:
    def intersection(a: ListNode, b: ListNode) -> Optional[ListNode]: 
        i, j = a, b
        while i != j:
            i = i.next if i else b
            j = j.next if j else a
        return i