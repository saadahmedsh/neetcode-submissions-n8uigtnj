# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:

        
        fast, slow = head, head

        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next

        second_half = slow.next
        slow.next = None

        prev = None
        curr = second_half

        while curr:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp

        first, second = head, prev
        while first and second:
            tmp1, tmp2 = first.next, second.next
            first.next = second
            second.next = tmp1
            first = tmp1
            second = tmp2



                                
                                
        