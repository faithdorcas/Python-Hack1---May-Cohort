class QueueWithStacks:
    def __init__(self):
        self.stack_in = []  # Stack for enqueue operations
        self.stack_out = []  # Stack for dequeue operations

    def enqueue(self, x: int):
        self.stack_in.append(x)

    def dequeue(self) -> int:
        # If stack_out is empty, transfer elements from stack_in to stack_out
        if not self.stack_out:
            while self.stack_in:
                self.stack_out.append(self.stack_in.pop())
        if not self.stack_out:
            raise IndexError("Queue is empty")
        return self.stack_out.pop()

# Example usage
q = QueueWithStacks()
q.enqueue(1)
q.enqueue(2)
print(q.dequeue())  # Output: 1
print(q.dequeue())  # Output: 2