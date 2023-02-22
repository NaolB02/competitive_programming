# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        dumm2 = dummy
        
        if not head:
            return
        
        prev = head
        cur = head.next
        
        while cur:
            if prev.val == cur.val:
                while cur and prev.val == cur.val:
                    prev.next = cur.next
                    cur = cur.next
                
                dummy.next = prev.next
                
                if cur:
                    prev = prev.next
                    cur = cur.next
            
            else:
                prev = prev.next
                cur = cur.next
                dummy = dummy.next
        
        return dumm2.next
                
            
            