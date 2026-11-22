# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        curr = head
        nago = None
        for i in range(n):
            curr = curr.next
        if not curr:
            return head.next
        nago = head
        while (curr.next):
            curr = curr.next
            nago = nago.next
        if n != 1:
            nago.next = nago.next.next
        else:
            nago.next = None
        return head