from typing import Optional, ListNode
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode],  
                      list2: Optional[ListNode]) \
                        -> Optional[ListNode]:
        result = ListNode()
        head = result
        while list1 != None and list2 != None:
            if list1.val <= list2.val:
                result.next = list1
                list1 = list1.next
            else:
                result.next = list2
                list2 = list2.next
            result = result.next
        
        if list1 == None:
            result.next = list2
        else:
            result.next = list1

        return head.next