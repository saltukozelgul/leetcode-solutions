# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:

        # Find the length of the linked list
        length = 0
        current = head
        while current:
            length += 1
            current = current.next

        # If the length of the linked list is 1, return None
        if length == 1:
            return None

        # If the length of the linked list is equal to n, return the second node
        if length == n:
            return head.next

        # Find the node before the node to be removed
        current = head
        prev = None
        for _ in range(length - n):
            prev = current
            current = current.next
        
        # Remove the node
        prev.next = current.next

        return head
            