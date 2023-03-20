# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        slow, fast = head, head
        max_sum = 0

        # Get middle of linked list
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
        
        # Reverse from the middle of the linked list
        rev_head = None
        slow_ref = slow
        
        while slow_ref:
            slow_ref.next, rev_head, slow_ref = rev_head, slow_ref, slow_ref.next
            # rev_cur = ListNode(slow_ref.val, rev_head)
            # rev_head = rev_cur
            # slow_ref = slow_ref.next
                
        #find the maximum sum of twins
        while rev_head and head:
            max_sum = max(max_sum, rev_head.val + head.val)
            rev_head = rev_head.next
            head = head.next
        
        return max_sum