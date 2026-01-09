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

def find_length(head):
    # given head of linked list find number of nodes in linked list
    i = 0
    cur = head # we don't need head so we can techincally skip cur but just to maintain head in good state
    while cur:
        i += 1
        cur = cur.next
    
    return i

def mergeTwoLists(list1, list2):
    dummy = Node(-1)
    cur = dummy

    l1, l2 = list1, list2

    while l1 and l2:
        while l1 and l1.val <= l2.val:
            cur.next = Node(l1.val)
            l1 = l1.next
            cur = cur.next
        cur.next = Node(l2.val)
        l2 = l2.next
        cur = cur.next
    
    remaining = l1 if l1 else l2
    cur.next = remaining if remaining else None

    return dummy.next


l1 = make_linked_list([1, 2, 4, 5, 7])
l2 = make_linked_list([1, 3, 4])

# l1, l2 = make_linked_list([]), make_linked_list([])
# l1, l2 = make_linked_list([]), make_linked_list([0])

l3 = mergeTwoLists(l1, l2)
print_linked_list(l3)