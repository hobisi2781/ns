class DynamicArray:
    _arr: list[int]
    _tail: int
    _cap: int
    
    def __init__(self, capacity: int):
        self._arr = [0] * capacity
        self._cap = capacity
        self._tail = -1


    def get(self, i: int) -> int:
        return self._arr[i]


    def set(self, i: int, n: int) -> None:
        self._arr[i] = n


    def pushback(self, n: int) -> None:
        if self.getSize() >= self.getCapacity():
            self.resize()
        self._tail += 1
        self._arr[self._tail] = n



    def popback(self) -> int:
        val = self._arr[self._tail]
        self._tail -= 1
        return val
 

    def resize(self) -> None:
        self._cap *= 2
        new_arr = [0] * self._cap

        for i in range(self.getSize()):
            new_arr[i] = self._arr[i]
        
        self._arr = new_arr


    def getSize(self) -> int:
        return self._tail + 1
        
    
    def getCapacity(self) -> int:
        return self._cap
