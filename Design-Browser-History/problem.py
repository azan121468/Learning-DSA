class Node:
    def __init__(self, val=None, prev=None, next=None):
        self.val  = val
        self.prev = prev
        self.next  = next

class BrowserHistory:

    def __init__(self, homepage: str):
        self.cur = Node(homepage)
        # print(self.cur.val)

    def visit(self, url: str) -> None:
        # remove all the forward history from current node
        self.cur.next = None
        tmp = self.cur

        # create new node, set next field of previous node and prev field of current node
        page = Node(url)
        self.cur.next = page
        self.cur = page
        self.cur.prev = tmp

    def back(self, steps: int) -> str:
        i = 0
        while self.cur and self.cur.prev and i < steps: # should also add and condition of self.cur.prev should exist so that prev doesn't point to null but this is extra
            self.cur = self.cur.prev
            i += 1
        return self.cur.val

    def forward(self, steps: int) -> str:
        i = 0
        while self.cur and self.cur.next and i < steps:
            self.cur = self.cur.next
            i += 1
        return self.cur.val

x = BrowserHistory("leetcode.com")
