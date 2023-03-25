# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head or not head.next:
            return head
        
        last = head
        size = 0
        # find the last node
        while last and last.next:
            size += 1
            last = last.next
        
        size += 1        
        last.next = head
        # find the right amount of k
        k = k % size
        k = size - k - 1
        
        # find the new head
        for _ in range(k):
            head = head.next

        start = head.next
        head.next = None

        return start
        
            