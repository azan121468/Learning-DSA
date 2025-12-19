
class Node:
    def __init__(self, val=None, prev=None, next=None):
        self.val  = val
        self.prev = prev
        self.next  = next

if __name__ == "__main__":
    n1 = Node(1)
    n2 = Node(2, n1)
    n3 = Node(3, n2)
    n4 = Node(4, n3)
    n5 = Node(5, n4)

    n1.next = n2
    n2.next = n3
    n3.next = n4
    n4.next = n5

    cur = n1
    print("Going forward")
    while cur:
        print(cur.val)
        tmp = cur
        cur = cur.next
        if cur:     # when end of linked list, cur is not a node but None which doesn't have prev field
            cur.prev = tmp

    print("Going backward")
    while cur:
        print(cur.val)
        cur = cur.prev