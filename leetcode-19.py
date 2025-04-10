from typing import Optional, List

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        fast = slow = head
        step = 0
        while True:
            if step <= n:
                fast = fast.next
                step += 1
            else:
                fast = fast.next
                slow = slow.next
                step += 1

            if fast == None:
                if n >= step:
                    return head.next
                else:
                    slow.next = slow.next.next
                    return head


            