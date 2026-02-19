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

def find_middle(head):
    slow, fast = head, head.next
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
    return slow

def merge(l1, l2):
    '''Merge two sorted linked lists'''
    dummy_node = Node()
    cur = dummy_node

    while l1 and l2:
        if l2.val > l1.val:
            cur.next = l1
            l1 = l1.next
        else:
            cur.next = l2
            l2 = l2.next
        
        cur = cur.next
    
    cur.next = l1 if l1 else l2
    
    return dummy_node.next

def sortList(head):
    if not head or not head.next:
        return head
    
    middle_node = find_middle(head)
    l, r = head, middle_node.next
    middle_node.next = None

    left_sort = sortList(l)
    right_sort = sortList(r)

    sorted_list = merge(left_sort, right_sort)

    return sorted_list

# Merge testing
# print_linked_list(merge(make_linked_list([1,2,3,10,5]), make_linked_list([6,7,8,9,10])))

a = make_linked_list([3,5,1,2,4])
print_linked_list(sortList(a))