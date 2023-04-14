# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        cur = head
        size = 0
        
        while head:
            head = head.next
            size += 1
        
        if size < 2:
            return cur
        
        return self.mergeLL(cur, size)
    
    def mergeLL(self, head: Optional[ListNode], size: int) -> Optional[ListNode]:
        cur = head
        
        if size == 1:
            cur = ListNode(head.val)
            return cur
        
        left = self.mergeLL(cur, size // 2)
        
        for _ in range(0, size // 2):
            cur = cur.next
            
        right = self.mergeLL(cur, size - (size // 2))
        
        return self.merge(left, right)
    
    def merge(self, left: Optional[ListNode], right: Optional[ListNode]) -> Optional[ListNode]:
        merged = ListNode()
        cur = merged
        
        while left and right:
            if left.val <= right.val:
                cur.next = ListNode(left.val)
                left = left.next
            
            else:
                cur.next = ListNode(right.val)
                right = right.next
            
            cur = cur.next
        
        while left:
            cur.next = ListNode(left.val)
            left = left.next
            cur = cur.next
        
        while right:
            cur.next = ListNode(right.val)
            right = right.next
            cur = cur.next
        
        return merged.next