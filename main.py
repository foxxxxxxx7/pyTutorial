from collections import deque


class BufferFullException(BufferError):
    def __init__(self, message="Circular buffer is full"):
        super().__init__(message)


class BufferEmptyException(BufferError):
    def __init__(self, message="Circular buffer is empty"):
        super().__init__(message)


class CircularBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        self.buffer = deque(maxlen=capacity)

    def read(self):
        if len(self.buffer) == 0:
            raise BufferEmptyException()
        return self.buffer.popleft()

    def write(self, data):
        if len(self.buffer) == self.capacity:
            raise BufferFullException()
        self.buffer.append(data)

    def overwrite(self, data):
        if len(self.buffer) == self.capacity:
            self.buffer.popleft()
        self.buffer.append(data)

    def clear(self):
        self.buffer.clear()
