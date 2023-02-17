# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        length = 0
        newHead = ListNode()
        cur = newHead
        
        while head:
            cur.next = ListNode(head.val)
            cur = cur.next
            head = head.next
            length += 1
        
        fromEnd = length - n
        cur = newHead
        
        for _ in range(fromEnd):
            cur = cur.next
        
        cur.next = cur.next.next
        return newHead.next
        
        