from string import ascii_letters
from random import choice

class Node:
    def __init__(self, value, left=None, right=None):
        self.val = value
        self.left = left
        self.right = right
    
    def __str__(self):
        return f"Node({self.val})"

def create_tree(node, cur_level, max_level):
    if cur_level == max_level:
        return

    l, r = choice(ascii_letters), choice(ascii_letters)
    
    node.left = Node(l)
    node.right = Node(r)

    create_tree(node.left, cur_level+1, max_level)
    create_tree(node.right, cur_level+1, max_level)

# def hide_word(node, word, i):
#     if not node or i >= len(word): return

#     node.val = word[i]

#     is_left = choice([0, 1])
#     if is_left:
#         hide_word(node.left, word, i+1)
#     else:
#         hide_word(node.right, word, i+1)

def hide_word(node, word, i):
    if not node or i >= len(word): 
        return

    node.val = word[i]

    # choose a child that exists
    if node.left and node.right:
        child = choice([node.left, node.right])
    elif node.left:
        child = node.left
    elif node.right:
        child = node.right
    else:
        return  # leaf reached

    hide_word(child, word, i+1)



string_to_find = 'azanshahid'
c = choice(ascii_letters)

root = Node(c)
create_tree(root, 0, len(string_to_find) - 1)

hide_word(root, string_to_find, 0)

#now find word in root