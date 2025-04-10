from typing import Optional, List


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        h1, h2 = l1, l2
        ls1, ls2 = [], []
        while h1 != None:
            ls1.append(str(h1.val))
            h1 = h1.next
        
        while h2 != None:
            ls2.append(str(h2.val))
            h2 = h2.next

        cl1 = reversed(ls1)
        cl2 = reversed(ls2)
        cl3 = str((int(''.join(cl1))) + (int(''.join(cl2))))
        l3 = ListNode()
        h3 = l3
        for c in reversed(cl3):
            h3.next = ListNode(int(c), None)
            h3 = h3.next
        return l3.next
        

