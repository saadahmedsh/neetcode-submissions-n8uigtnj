"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':

        curr = head
        copy_map = {}

        if not head:
            return None

        while curr:
            copy = Node(curr.val)
            copy_map[curr] = copy
            curr = curr.next

        curr = head
        while curr:
            copy = copy_map[curr]
            if curr.next:
                copy.next = copy_map[curr.next]
            else:
                copy.next = None

            if curr.random:
                copy.random = copy_map[curr.random]
            else:
                copy.random = None
            curr = curr.next

        return copy_map[head]


        