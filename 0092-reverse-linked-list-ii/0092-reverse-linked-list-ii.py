# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        startNode, curNode, endNode = ListNode(None, next = head), head, head
        startcount, curcount, endcount = 0, 1, 1
        
        while startcount < left - 1:
            startNode = startNode.next
            startcount += 1
        
        while endcount < right + 1:
            endNode = endNode.next
            endcount += 1
        
        while curcount < left:
            curNode = curNode.next
            curcount += 1
        
        revHead = ListNode(curNode.val, next = endNode)
        while curcount < right:
            curNode = curNode.next
            revcur = ListNode(curNode.val, revHead)
            revHead = revcur
            curcount += 1
        
        
        startNode.next = revHead
        if startNode.val == None:
            return startNode.next
        return head
        