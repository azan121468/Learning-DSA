# https://www.youtube.com/watch?v=Sbciimd09h4

class Node:
    def __init__(self, value, left=None, right=None):
        self.val = value
        self.left = left
        self.right = right
    
    def __str__(self):
        return f"Node({self.val})"

def tree1():
    r'''


                1
           /        \
         2            3
       /   \        /   \
     4      5      6     7
    / \    / \    / \   / \
   8   9 10  11 12 13 14 15

'''
    t8 = Node(8)
    t9 = Node(9)
    t10 = Node(10)
    t11 = Node(11)
    t12 = Node(12)
    t13 = Node(13)
    t14 = Node(14)
    t15 = Node(15)

    t4 = Node(4, t8, t9)
    t5 = Node(5, t10, t11)
    t6 = Node(6, t12, t13)
    t7 = Node(7, t14, t15)

    t2 = Node(2, t4, t5)
    t3 = Node(3, t6, t7)

    t1 = Node(1, t2, t3)

    root = t1

    return root

def tree2():
    r'''


                1
           /        \
         2            3
       /   \        /   \
     4      5      6     7
    / \           /       \
   8   9        12        15

'''
    t8 = Node(8)
    t9 = Node(9)
    t12 = Node(12)
    t15 = Node(15)

    t4 = Node(4, t8, t9)
    t5 = Node(5)
    t6 = Node(6, t12)
    t7 = Node(7, t15)

    t2 = Node(2, t4, t5)
    t3 = Node(3, t6, t7)

    t1 = Node(1, t2, t3)

    root = t1

    return root

root = tree2()