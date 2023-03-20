# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        # find the length
        n = 0
        current = head
        
        while current != None:
            n += 1
            current = current.next
        
        # initialize the array that holds the twins
        twins = []
        index = 0
        current = head
        
        # find the twins and store them in twins
        while current != None:
            if index < (n // 2):
                twins.append([current.val, -1])
            
            else:
                twins[(-index) + n - 1][1] = current.val
            
            current = current.next
            index += 1
        
        max_sum = sum(max(twins, key=lambda x: sum(x)))
        return max_sum