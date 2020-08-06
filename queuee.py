from exception import Empty

class queue:
    def __init__(self):
        self.first = 0
        self.size = 0
        self.data = []

    def __len__(self):
        return self.size

    def _isempty(self):
        return self.size == 0

    def enqueue(self, val):
        self.data.append(val)
        self.size += 1

    def dequeue(self):
        value = self.data[self.first]
        self.data[self.first] = None
        self.first += 1
        self.size -= 1
        return value

    def display(self):
        print(self.data)


