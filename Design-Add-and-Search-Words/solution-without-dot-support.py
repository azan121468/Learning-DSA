class PrefixTree:
    def __init__(self, char='', isEnd=False):
        self.char = char
        self.next = {}   # next character: node of next character
        self.isEnd = isEnd

class WordDictionary:

    def __init__(self):
        self.tree = PrefixTree()

    def addWord(self, word: str) -> None:
        head = self.tree
        for char in word:
            if char in head.next.keys():
                head = head.next[char]
            else:
                head.next[char] = PrefixTree(char)
                head = head.next[char]
        head.isEnd = True

    def search(self, word: str) -> bool:
        head = self.tree
        for char in word:
            if char in head.next.keys():
                head = head.next[char]
            else:
                return False
        return head.isEnd

c = WordDictionary()
c.addWord('Azan')
assert c.search('Azan')
assert not c.search('Shahid')
c.addWord('Shahid')
assert not c.search('AzanShahidHacker')
assert not c.search('ShahidHacker')