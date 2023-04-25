# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        total = int(self.getNumber(l1)) + int(self.getNumber(l2))
        ## I have 807 and want to convert [7,0,8]
        strList = list(str(total)[::-1])
        ## Now we have ['7','0','8'] and we want to convert to [7,0,8]
        return [int(i) for i in strList]

    def getNumber(self,node):
        if (node.next != None):
            return  self.getNumber(node.next) + str(node.val)
        else:
            return str(node.val)