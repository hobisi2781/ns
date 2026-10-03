class TreeNode:
    def __init__(self, key: int, val: int, next_node: TreeNode | None = None):
        self.key = key
        self.val = val
        self.next = next_node

class MyHashMap:
    size = 1000 # 1_000_000 * ((1/2) ** 4); 1000 slots, <= 4 in each
    _arr: list[TreeNode | None]

    def __init__(self):
        self._arr = [None] * self.size
        

    def put(self, key: int, value: int) -> None:
        index = self._hash(key)

        node = self._arr[index]

        if not node:
            self._arr[index] = TreeNode(key, value)
            return
        
        temp = node
        while temp:
            if temp.key == key:
                temp.val = value
                break
            if temp.next: 
                temp = temp.next
            else:
                temp.next = TreeNode(key, value)
        
        self._arr[index] = node

        

    def get(self, key: int) -> int:
        index = self._hash(key)
        node = self._arr[index]

        if not node:
            return -1
        
        temp = node
        while temp:
            if temp.key == key:
                return temp.val
            temp = temp.next
        
        return -1
        

    def remove(self, key: int) -> None:
        index = self._hash(key)
        node = self._arr[index]

        if not node:
            return
        
        temp = node
        prev: TreeNode | None = None

        while temp:
            if temp.key != key:
                prev = temp
                temp = temp.next
                continue
            
            if not prev:
                node = None
                break
            
            prev.next = temp.next
            break
        
        self._arr[index] = node
            

    def _hash(self, key: int) -> int:
        return key % self.size
        


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)