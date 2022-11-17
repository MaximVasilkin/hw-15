class Stack:

    def __init__(self, data=None):
        self.data = [item for item in data] if data else []
        self.data.reverse()

    def __iter__(self):
        self.counter = 0
        self.iter = iter(self.data)
        return self

    def __next__(self):
        if self.counter + 1 > self.size():
            raise StopIteration
        element = next(self.iter)
        self.counter += 1
        return element

    def IsEmpty(self):
        return True if not self.data else False

    def push(self, element):
        self.data += [element]

    def pop(self):
        last_element = self.data[-1]
        self.data = self.data[:-1]
        return last_element

    def peek(self):
        return self.data[-1]

    def size(self):
        return len(self.data)

    def __str__(self):
        info = str(self.data)[1:-1]
        return info if info else 'Stack is empty'