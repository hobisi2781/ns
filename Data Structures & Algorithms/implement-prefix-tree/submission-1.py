class TrieNode:
    char: str
    children: list[TrieNode]
    complete: bool

    def __init__(self, char: str, complete=False):
        self.char = char
        self.complete = complete
        self.children = []

class PrefixTree:
    root: TrieNode

    def __init__(self):
        self.root = TrieNode('')

    def insert(self, word: str) -> None:
        temp = self.root

        for char in word:
            found = False
            for child in temp.children:
                if child.char == char:
                    found = True
                    temp = child
            
            if not found:
                node = TrieNode(char)
                temp.children.append(node)
                temp = node
        
        temp.complete = True
        

    def search(self, word: str) -> bool:
        temp = self.root
        
        for char in word:
            found = False
            for child in temp.children:
                if child.char == char:
                    found = True
                    temp = child
                    break
            if not found:
                return False 

        return temp.complete
        

    def startsWith(self, prefix: str) -> bool:
        temp = self.root

        for char in prefix:
            found = False
            for child in temp.children:
                if child.char == char:
                    found = True
                    temp = child
                    break
            
            if not found:
                return False
        
        return True

        
        