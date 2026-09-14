class DynamicArray:
    
    def __init__(self, capacity: int):
        self.list = [0] * capacity
        self.capacity = capacity
        self.size = 0

    def get(self, i: int) -> int:
        return self.list[i]

    def set(self, i: int, n: int) -> None:
        self.list[i] = n

    def pushback(self, n: int) -> None:
        if self.size == self.capacity:
            self.resize()
        self.list[self.size] = n
        self.size += 1

    def popback(self) -> int:
        self.size -= 1
        return self.list[self.size]

    def resize(self) -> None:
        self.capacity *= 2
        new_list = [0] * self.capacity
        for i in range(self.size):
            new_list[i] = self.list[i]
        self.list = new_list

    def getSize(self) -> int:
        return self.size
    
    def getCapacity(self) -> int:
        return self.capacity