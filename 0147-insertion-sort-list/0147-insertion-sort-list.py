# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def insertionSortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = head
        cur = head.next
        
        while cur:
            cur_prev = None
            cur_cur = head
            
            while cur_cur and cur_cur.val < cur.val:
                if not cur_prev: cur_prev = head
                else: cur_prev = cur_prev.next
                cur_cur = cur_cur.next
            
            if cur_cur == cur:
                prev = prev.next
                cur = cur.next
                continue
            
            if cur_prev:
                cur_prev.next = ListNode(cur.val, cur_cur)
            
            else:
                head = ListNode(cur.val, head)
            
            prev.next = cur.next
            cur = prev.next
            
        return head
            
            