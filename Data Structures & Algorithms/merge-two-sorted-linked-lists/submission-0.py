# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if not list1:
            return list2
        if not list2:
            return list1
        curr1, curr2 = list1, list2
        if curr1.val < curr2.val:
            newlist = curr1
            curr1 = curr1.next
        else:
            newlist = curr2
            curr2 = curr2.next
        newhead = newlist
        while curr1 or curr2:
            if curr1 and curr2:
                if curr1.val < curr2.val:
                    newlist.next = curr1
                    newlist = newlist.next
                    curr1 = curr1.next
                else:
                    newlist.next = curr2
                    newlist = newlist.next
                    curr2 = curr2.next
            elif curr1:
                newlist.next = curr1
                newlist = newlist.next
                curr1 = curr1.next
            else:
                newlist.next = curr2
                newlist = newlist.next
                curr2 = curr2.next
        return newhead