# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:

        dummy = ListNode()
        pointer = dummy

        while True:
            minimum = float('inf')
            index = -1
            for i in range(len(lists)):
                if lists[i] and lists[i].val < minimum:
                    minimum = lists[i].val
                    index = i
            if index == -1:
                break
            pointer.next = lists[index]
            lists[index] = lists[index].next
            pointer = pointer.next

        return dummy.next