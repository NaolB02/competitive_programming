class DNode:
    
    def __init__(self, val='', prev=None, next=None):
        self.val = val
        self.prev = prev
        self.next = next
        
class BrowserHistory:

    def __init__(self, homepage: str):
        self.homepage = DNode(homepage)
        self.curNode = self.homepage

    def visit(self, url: str) -> None:
        browser = DNode(url, self.curNode, None)
        self.curNode.next = browser
        self.curNode = self.curNode.next

    def back(self, steps: int) -> str:
        while steps and self.curNode.prev:
            self.curNode = self.curNode.prev
            steps -= 1
        
        return self.curNode.val

    def forward(self, steps: int) -> str:
        while steps and self.curNode.next:
            self.curNode = self.curNode.next
            steps -= 1
        
        return self.curNode.val


# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)