# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # phase - 1
        rabbit = tortoise = head
        
        if not rabbit:
            return rabbit
        
        elif not rabbit.next:
            return rabbit.next
        
        while rabbit and rabbit.next:
            rabbit = rabbit.next.next
            tortoise = tortoise.next
            
            if rabbit == tortoise:
                break
        
        # phase - 2
        tortoise = head
        while rabbit and tortoise and rabbit != tortoise:
            tortoise = tortoise.next
            rabbit = rabbit.next
        
        return rabbit