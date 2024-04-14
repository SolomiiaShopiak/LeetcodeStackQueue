class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Queue:
    def __init__(self):
        self.front = None
        self.rear = None
        self.size = 0

    def is_empty(self):
        return self.size == 0

    def add(self, item):
        new_node = Node(item)
        if self.is_empty():
            self.front = new_node
        else:
            self.rear.next = new_node
        self.rear = new_node
        self.size += 1

    def pop(self):
        if self.is_empty():
            raise IndexError("Queue is empty")
        data = self.front.data
        self.front = self.front.next
        self.size -= 1
        if self.is_empty():
            self.rear = None
        return data

    def peek(self):
        if self.is_empty():
            raise IndexError("Queue is empty")
        return self.front.data

    def __len__(self):
        return self.size

class MyStack:
    def __init__(self):
        self.queue1 = Queue()
        self.queue2 = Queue()

    def push(self, x: int) -> None:
        self.queue1.add(x)

    def pop(self) -> int:
        if self.empty():
            return None
        
        while len(self.queue1) > 1:
            self.queue2.add(self.queue1.pop())

        popped_element = self.queue1.pop()

        self.queue1, self.queue2 = self.queue2, self.queue1
        return popped_element

    def top(self) -> int:
        if self.empty():
            return None

        while len(self.queue1) > 1:
            self.queue2.add(self.queue1.pop())

        top_element = self.queue1.peek()

        self.queue2.add(self.queue1.pop())

        self.queue1, self.queue2 = self.queue2, self.queue1

        return top_element

    def empty(self) -> bool:
        return len(self.queue1) == 0
