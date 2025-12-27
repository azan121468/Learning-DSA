import random

class TrieNode:
    def __init__(self, is_end=False):
        self.next = {}   # next character: node of next character
        self.is_end = is_end  #PEP8

class Trie:
    def __init__(self):
        self.head = TrieNode()

    def insert(self, word: str) -> None:
        cur = self.head

        for char in word:
            if char not in cur.next:
                cur.next[char] = TrieNode()
            cur = cur.next[char]

        cur.is_end = True

    def search(self, word: str, search_full_word: bool = True) -> bool:
        #search_full_word argument is required to make prefix check possible without requiring additional function. 
        cur = self.head

        for char in word:
            if char not in cur.next:
                return False
            cur = cur.nxt[char]
        
        return cur.is_end if search_full_word else True

    def startsWith(self, prefix: str) -> bool:
        return self.search(prefix, search_full_word=False)

c = Trie()

to_insert = ['Azan', 'Shahid', 'Testing', '1234', 'ABCDEF']
for val in to_insert:
    c.insert(val)

assert c.search(random.choice(to_insert))
assert c.search('Azan')

random_choice = random.choice(to_insert)
random_prefix = random_choice[:random.choice(range(0, len(random_choice)-1))]
assert c.startsWith(random_prefix)
assert not c.startsWith(f'x{random_prefix}')
assert not c.startsWith(f'{random_prefix}x')