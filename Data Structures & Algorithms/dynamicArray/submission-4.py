class DynamicArray:
    
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.size = 0
        self.arr = [0] * capacity


    def get(self, i: int) -> int:
        if self.size > i:
            return self.arr[i]

    def set(self, i: int, n: int) -> None:
        if self.size > i:
            self.arr[i] = n

    def pushback(self, n: int) -> None:
        if self.size == self.capacity:
            self.resize()
        self.arr[self.size] = n
        self.size += 1


    def popback(self) -> int:
        if self.arr!=[]:
            removed = self.arr[self.size-1]
            self.size -= 1
            return removed

    def resize(self) -> None:
        new_arr = [0] * self.capacity
        for i in range(self.size):
            new_arr[i] = self.arr[i]
        self.arr = new_arr
        self.arr = self.arr * 2
        self.capacity *= 2

    def getSize(self) -> int:
        return self.size
    
    def getCapacity(self) -> int:
        return self.capacity
