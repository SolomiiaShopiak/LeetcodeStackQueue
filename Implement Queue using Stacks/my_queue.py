class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class Stack:
    def __init__(self):
        self.top = None

    def push(self, value):
        new_node = Node(value)
        new_node.next = self.top
        self.top = new_node

    def pop(self):
        if self.top is None:
            return None
        value = self.top.value
        self.top = self.top.next
        return value

    def peek(self):
        if self.top is None:
            return None
        return self.top.value

    def is_empty(self):
        return self.top is None

class MyQueue:
    def __init__(self):
        self.stack_push = Stack()
        self.stack_pop = Stack()

    def push(self, item: int) -> None:
        self.stack_push.push(item)

    def pop(self) -> int:
        if self.stack_pop.is_empty():
            while not self.stack_push.is_empty():
                self.stack_pop.push(self.stack_push.pop())
        return self.stack_pop.pop()

    def peek(self) -> int:
        if self.stack_pop.is_empty():
            while not self.stack_push.is_empty():
                self.stack_pop.push(self.stack_push.pop())
        return self.stack_pop.peek()

    def empty(self) -> bool:
        return self.stack_push.is_empty() and self.stack_pop.is_empty()
