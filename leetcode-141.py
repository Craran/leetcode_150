from typing import Optional, Dict, Set
# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if not head or not head.next:
            return False
        
        ids: Set[int] = set()

        point: Optional[ListNode] = head
        while point and point.next:
            if id(point) not in ids:
                ids.add(id(point))
                point = point.next
                continue
            if id(point) in ids:
                return True
            
        return False







"""
最大n步就会相遇，命题等价为：
对有限域[0, n-1]，找到k使得k = 2k mod n
则k = 0 mod n
"""