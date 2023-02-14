# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        curNode = head
        arr = []
        while curNode != None:
            arr.append(curNode.val)
            curNode = curNode.next
        
        if arr == []:
            return True

        start, end = 0, len(arr) - 1

        while start < end:
            if arr[start] == arr[end]:
                start += 1
                end -= 1
            else:
                return False
        
        return True