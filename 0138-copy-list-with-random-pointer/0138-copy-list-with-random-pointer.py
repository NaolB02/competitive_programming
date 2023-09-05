"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        newHead = Node(0)
        
        cur = head
        while cur:
            cur.next = Node(cur.val, cur.next)
            cur = cur.next.next
        
        nullNode = None
        
        cur2 = head
        while cur2:
            if cur2.random:
                cur2.next.random = cur2.random.next
            
            else:
                cur2.next.random = nullNode
            
            cur2 = cur2.next.next
            
        cur3 = newHead
        while head:
            cur3.next = head.next
            head = head.next.next
            cur3 = cur3.next
        
        cur3.next = nullNode
        return newHead.next
            
        
        