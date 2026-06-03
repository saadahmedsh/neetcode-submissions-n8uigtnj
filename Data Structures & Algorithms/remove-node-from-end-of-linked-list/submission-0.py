# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        curr = head
        for i in range(n):
            curr = curr.next
            
        dummy = ListNode()
        dummy.next = head

        prev_pointer = dummy

        while curr:
            curr = curr.next
            prev_pointer = prev_pointer.next

        prev_pointer.next = prev_pointer.next.next

        return dummy.next
        
        