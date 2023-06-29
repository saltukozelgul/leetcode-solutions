# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
            if not head or k == 1:
                return head
            
            dummy = ListNode(0)
            dummy.next = head
            
            prev = dummy
            curr = head
            i = 0
            
            while curr:
                i += 1
                
                if i % k == 0:
                    prev = self.reverse(prev, curr.next)
                    curr = prev.next
                else:
                    curr = curr.next
            
            return dummy.next

    def reverse(self, prev, next):
        last = prev.next
        curr = last.next
        
        while curr != next:
            last.next = curr.next
            curr.next = prev.next
            prev.next = curr
            curr = last.next
        
        return last

