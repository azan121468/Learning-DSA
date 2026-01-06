class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
    
    def __str__(self):
        return f"Node({self.val})"

#Tree1: leet code example
r'''
          6
        /    \
       2      8
      / \    / \
     0   4  7   9
        / \
       3   5
'''

#Tree2: leet code example
r'''
            6
         /     \
       2        8
      / \      / \
     0   4    7   9
        / \
       3   5
'''
#asked gpt to made for me.
# ----------------------
# Tree1
# ----------------------

# Individual nodes named by value
n6 = Node(6)
n2 = Node(2)
n8 = Node(8)
n0 = Node(0)
n4 = Node(4)
n7 = Node(7)
n9 = Node(9)
n3 = Node(3)
n5 = Node(5)

# Connecting children
n4.left = n3
n4.right = n5

n2.left = n0
n2.right = n4

n8.left = n7
n8.right = n9

n6.left = n2
n6.right = n8

# Root of Tree1
root1 = n6

# ----------------------
# Tree2
# ----------------------

# Individual nodes named by value
m6 = Node(6)
m2 = Node(2)
m8 = Node(8)
m0 = Node(0)
m4 = Node(4)
m7 = Node(7)
m9 = Node(9)
m3 = Node(3)
m5 = Node(5)

# Connecting children
m4.left = m3
m4.right = m5

m2.left = m0
m2.right = m4

m8.left = m7
m8.right = m9

m6.left = m2
m6.right = m8

# Root of Tree2
root2 = m6