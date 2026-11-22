# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        # the last element will be the n//2 element
        count = 0
        node = head
        while (node):
            count += 1
            node = node.next
        mid = count // 2
        node = head
        for i in range(mid):
            node = node.next
        half2 = node.next
        node.next = None
        prev, curr = None, half2
        while (half2):
            temp = half2.next
            half2.next = prev
            prev = half2
            half2 = temp
        ins = prev
        curr = head
        # 0, 1, 2, 3
        # 6, 5, 4
        while ins:
            tempins = ins.next
            ins.next = curr.next
            curr.next = ins
            ins = tempins
            curr = curr.next.next
