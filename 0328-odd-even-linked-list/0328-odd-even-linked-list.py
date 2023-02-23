# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        oddNodes = ListNode()
        oddcur = oddNodes
        
        evenNodes = ListNode()
        evencur = evenNodes
        
        count = 1
        
        while head:
            if count % 2 != 0:
                oddcur.next = ListNode(head.val)
                oddcur = oddcur.next
            
            else:
                evencur.next = ListNode(head.val)
                evencur = evencur.next
            
            head = head.next
            count += 1
        
        oddcur.next = evenNodes.next
        return oddNodes.next