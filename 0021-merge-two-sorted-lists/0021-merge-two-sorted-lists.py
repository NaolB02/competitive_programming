# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        
        def merger(list1, list2, head = ListNode(-101), main = ListNode()):
            if head.val == -101:
                main.next = head
                head.val = 0
                merger(list1, list2, head, main)
                return main
                
            elif not list1:
                head.next = list2
                return main
            
            elif not list2:
                head.next = list1
                return main
            
            elif list1.val > list2.val:
                head.next = ListNode(list2.val)
                list2 = list2.next
                head = head.next
                
                return merger(list1, list2, head)
            
            else:
                head.next = ListNode(list1.val)
                list1 = list1.next
                head = head.next
                
                return merger(list1, list2, head)
        
        return merger(list1, list2).next.next