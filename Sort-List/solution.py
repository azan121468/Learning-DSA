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

def sortList(head):
    #single or empty node is considered sorted, so return as it is
    if not head or not head.next:
        return head
    
    #find the middle to break the list into two lists
    slow, fast = head, head.next
    while fast and fast.next:
        slow, fast = slow.next, fast.next.next
    
    #slow is the node before middle. This is from where, we will split the linked list
    l, r = head, slow.next
    slow.next = None

    #sort both lists
    left_sort = sortList(l)
    right_sort = sortList(r)

    #merge them
    dummy_node = Node()
    l1, l2 = left_sort, right_sort
    cur = dummy_node

    while l1 and l2:
        if l1.val < l2.val:
            cur.next = l1
            l1 = l1.next
        else:
            cur.next = l2
            l2 = l2.next        
        cur = cur.next
    
    cur.next = l1 if l1 else l2

    #return head of merged list
    return dummy_node.next

a = make_linked_list([3,5,1,2,4])
print_linked_list(sortList(a))