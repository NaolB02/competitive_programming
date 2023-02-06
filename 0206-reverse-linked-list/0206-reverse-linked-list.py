# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        nums = []
        
        while head:
            nums.append(head.val)
            head = head.next
        
        nums.reverse()
        revHead = ListNode()
        curNode = revHead
        
        for num in nums:
            curNode.next = ListNode(num)
            curNode = curNode.next
        
        return revHead.next