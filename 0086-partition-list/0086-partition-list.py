# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        # new ll that will be returned
        newHead = ListNode()
        cur = newHead
        # ll containing all elements in the original ll above x
        biggerThanx = ListNode()
        curb = biggerThanx
        
        while head:
            if head.val < x:
                cur.next = ListNode(head.val)
                cur = cur.next
            
            else:
                curb.next = ListNode(head.val)
                curb = curb.next
            
            head = head.next
        
        # joining the two lls
        # above x and below x
        cur.next = biggerThanx.next
        return newHead.next