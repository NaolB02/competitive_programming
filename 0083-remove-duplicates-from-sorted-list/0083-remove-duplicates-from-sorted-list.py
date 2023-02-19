# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:        
        curNode = head
        
        while curNode and curNode.next:
            if curNode.val == curNode.next.val:
                curNode.next = curNode.next.next
            
            else:
                curNode = curNode.next
        
        return head
        