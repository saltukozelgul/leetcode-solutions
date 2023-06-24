# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:

        # create a dummy node
        dummy = ListNode()
        # create a pointer to dummy
        pointer = dummy

        # while both lists are not empty
        while list1 and list2:
            # if list1's value is smaller than list2's value
            if list1.val < list2.val:
                # set pointer's next to list1
                pointer.next = list1
                # move list1's pointer to next
                list1 = list1.next
            # if list2's value is smaller than list1's value
            else:
                # set pointer's next to list2
                pointer.next = list2
                # move list2's pointer to next
                list2 = list2.next
            # move pointer to next
            pointer = pointer.next

        # if list1 is not empty
        if list1:
            # set pointer's next to list1
            pointer.next = list1
        # if list2 is not empty
        if list2:
            # set pointer's next to list2
            pointer.next = list2

        # return dummy's next
        return dummy.next