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

def rotateRight(head, k):
    if not head or k == 0:
        return head
    
    #1. Find length of linked list
    length = 0
    prev, cur = None, head
    while cur:
        length += 1
        prev = cur
        cur = cur.next
    last = prev  # we will need it for linking at end
    
    #2. Find how much to rotate
    k = k % length
    if k == 0:  #no rotation needed
        return head

    #3. Move to node whose next is new head (effectively tail of new list)
    cur = head
    for _ in range(length - k - 1):
        cur = cur.next
    
    #4. relink the head
    new_head = cur.next
    cur.next = None
    last.next = head

    return new_head




ll = make_linked_list([1,2,3,4,5,6,7,8,9,10])
rotated_ll = rotateRight(ll, 12)
print_linked_list(rotated_ll)