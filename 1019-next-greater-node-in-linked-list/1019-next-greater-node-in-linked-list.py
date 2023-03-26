# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def nextLargerNodes(self, head: Optional[ListNode]) -> List[int]:      
        cur = head
        size = 0
        
        while cur:
            cur = cur.next
            size += 1
         
        next_gre_elements = [0] * size
        mon_stack = []
        index = 0
        
        while head:            
            while mon_stack and mon_stack[-1][0] < head.val:
                val, ind = mon_stack.pop()
                next_gre_elements[ind] = head.val
                
            mon_stack.append([head.val, index])
            index += 1
            head = head.next
        
        return next_gre_elements