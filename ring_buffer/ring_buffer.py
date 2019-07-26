class RingBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        self.current = 0
        self.storage = [None]*capacity

    def append(self, item):
        self.storage[self.current] = item
        self.current = (self.current + 1) % len(self.storage)
        print(self.current)

    def get(self):
        # result = []
        # for i in range(0, self.capacity):
        #     read = (self.current + i) % self.capacity
        #     if self.storage[read] is not None:
        #         result.append(self.storage[read])

        # return result
        return [n for n in self.storage if n is not None]
