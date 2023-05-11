# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        heap = []
        
        for head in lists:
            while head:
                heapq.heappush(heap, head.val)
                head = head.next
        
        new_head = ListNode()
        cur = new_head
        
        while heap:
            num = heapq.heappop(heap)
            cur.next = ListNode(num)
            cur = cur.next
        
        return new_head.next
            