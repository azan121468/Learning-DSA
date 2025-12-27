class Node:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
    
    def __str__(self):
        # return f"Node({self.val})"
        return f"{self.val}"

def make_linked_list(nums):
    if not nums: return None

    n = len(nums)
    head = Node(nums[0])
    cur = head

    for i in range(1, len(nums)): # since we already created head node.
        cur.next = Node(nums[i])
        cur = cur.next
    
    return head

def print_linked_list(head):
    cur = head
    while cur:
        print(f"{cur} {'->' if cur.next else ''} ", end='')
        cur = cur.next
    print()

def removeNthFromEnd(head, n):
    # I know naming might make it hard to read but for now this is what i can write myself.
 
    # Idea is to initialize two pointer p1 and p2.
    # move p1 n times. then run p1 and p2 simultaneously until p1 reach end.
    # at this point, p2 points to node you want to delete.
    # to handle edge case of first node, we also use dummy node and track
    # prev node as well to help us remove the current node.

    dummy_node = Node(-1, head)
    prev, p1, p2 = dummy_node, head, head

    for _ in range(n):
        p1 = p1.next
    
    while p1:
        p1 = p1.next
        prev = p2
        p2 = p2.next

    prev.next = p2.next

    return dummy_node.next


         
ll = make_linked_list([1, 2, 3, 4, 5, 6])
ans = removeNthFromEnd(ll, 6)
print_linked_list(ans)