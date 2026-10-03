class MyHashSet:
    size = 1000
    _arr: list[int]

    def __init__(self):
        self._arr = [[] for _ in range(self.size)]

        

    def add(self, key: int) -> None:
        index = key % self.size
        if key not in self._arr[index]:
            self._arr[index].append(key)
        

    def remove(self, key: int) -> None:
        index = key % self.size
        if key in self._arr[index]:
            self._arr[index].remove(key)
        

    def contains(self, key: int) -> bool:
        index = key % self.size
        return key in self._arr[index]
        


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)