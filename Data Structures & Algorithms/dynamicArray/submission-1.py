class DynamicArray:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.size = 0
        self.arr = [None] * capacity

    def get(self, i: int) -> int:
        return self.arr[i]

    def set(self, i: int, n: int) -> None:
        self.arr[i] = n

    def pushback(self, n: int) -> None:
        # Resize before inserting if the array is full
        if self.size == self.capacity:
            self.resize()

        self.arr[self.size] = n
        self.size += 1

    def popback(self) -> int:
        self.size -= 1
        value = self.arr[self.size]

        # Optional: remove the stale reference/value
        self.arr[self.size] = None

        return value

    def resize(self) -> None:
        old_arr = self.arr

        self.capacity *= 2
        self.arr = [None] * self.capacity

        # Copy only the elements currently in the array
        for i in range(self.size):
            self.arr[i] = old_arr[i]

    def getSize(self) -> int:
        return self.size

    def getCapacity(self) -> int:
        return self.capacity