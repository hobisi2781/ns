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
        self._insert(word, 0, self.root)

    def _insert(self, word: str, index: int, node: TrieNode) -> None:
        char = word[index]

        childNode: TrieNode | None = None
        for child in node.children:
            if child.char == char:
                childNode = child
                break

        size = len(word)
        if childNode:
            if index + 1 != size:
                self._insert(word, index + 1, childNode)
            else:
                childNode.complete = True
        else:
            newNode = TrieNode(char)
            node.children.append(newNode)
            if index + 1 != size:
                self._insert(word, index + 1, newNode)
            else:
                newNode.complete = True

        



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

        
        