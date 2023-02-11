class Node:
    def __init__(self, val = 0, next = None):
        self.val = val
        self.next = next
        
class MyLinkedList:

    def __init__(self):
        self.head = Node()
        self.length = 0

    def get(self, index: int) -> int:
        if index >= self.length:
            return -1
        
        cur = self.head.next
        for _ in range(index):
            cur = cur.next
        
        return cur.val
        

    def addAtHead(self, val: int) -> None:
        cur = self.head.next
        newNode = Node(val, cur)
        self.head.next = newNode
        self.length += 1

    def addAtTail(self, val: int) -> None:
        cur = self.head
        while cur.next != None:
            cur = cur.next
        
        newNode = Node(val)
        cur.next = newNode
        self.length += 1

    def addAtIndex(self, index: int, val: int) -> None:
        if index > self.length:
            return -1
        
        cur = self.head
        for _ in range(index):
            cur = cur.next
        
        pushed = cur.next
        newNode = Node(val, pushed)
        cur.next = newNode
        self.length += 1
        

    def deleteAtIndex(self, index: int) -> None:
        if index >= self.length:
            return -1
        
        cur = self.head
        for _ in range(index):
            cur = cur.next
        
        cur.next = cur.next.next
        
        self.length -= 1
 
        


# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)