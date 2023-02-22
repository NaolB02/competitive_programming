# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        cur = ListNode()
        head = ListNode(0, cur)
        overflow = 0
        
        while l1 and l2:
            
            curSum = l1.val + l2.val + overflow
            
            if curSum >= 10:
                digit = curSum - 10
                overflow = 1
            
            else:
                digit = curSum
                overflow = 0
            
            cur.next = ListNode(digit)
            cur = cur.next
            l1 = l1.next
            l2 = l2.next
            
            if not l1:
                l1 = ListNode(0)
            
            elif not l2:
                l2 = ListNode(0)
        
        if overflow:
            cur.next = ListNode(1)
        
        return head.next.next
                