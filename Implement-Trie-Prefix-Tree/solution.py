# for this problem i just modified the solution i wrote for add and search word
import random

class TrieNode:
    def __init__(self, char='', isEnd=False):
        self.char = char
        self.next = {}   # next character: node of next character
        self.isEnd = isEnd

class Trie:

    def __init__(self):
        self.trie = TrieNode()

    def insert(self, word: str) -> None:
        head = self.trie
        for char in word:
            if char in head.next.keys():
                head = head.next[char]
            else:
                head.next[char] = TrieNode(char)
                head = head.next[char]
        head.isEnd = True

    def search(self, word: str) -> bool:
        head = self.trie
        for char in word:
            if char in head.next.keys():
                head = head.next[char]
            else:
                return False
        return head.isEnd

    def startsWith(self, prefix: str) -> bool:
        head = self.trie
        for char in prefix:
            if char not in head.next.keys():
                return False
            else:
                head = head.next[char]
        
        return True


c = Trie()

to_insert = ['Azan', 'Shahid', 'Hacker', 'AsliWalaHacker', 'Hacker']
for val in to_insert:
    c.insert(val)

assert c.search(random.choice(to_insert))
assert not c.search('Wala')

random_choice = random.choice(to_insert)
random_prefix = random_choice[:random.choice(range(0, len(random_choice)-1))]
assert c.startsWith(random_prefix)
assert not c.startsWith(f'x{random_prefix}')
assert not c.startsWith(f'{random_prefix}x')