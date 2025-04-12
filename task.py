from collections import deque

# -------------------- Stack using Queues --------------------
class MyStack(object):

    def __init__(self):
        self.first_queue = deque()
        self.second_queue = deque()

    def push(self, x):
        self.first_queue.append(x)

    def pop(self):
        while len(self.first_queue) > 1:
            self.second_queue.append(self.first_queue.popleft())
        top_element = self.first_queue.popleft()
        self.first_queue, self.second_queue = self.second_queue, self.first_queue
        return top_element

    def top(self):
        while len(self.first_queue) > 1:
            self.second_queue.append(self.first_queue.popleft())
        top_element = self.first_queue[0]
        self.second_queue.append(self.first_queue.popleft())
        self.first_queue, self.second_queue = self.second_queue, self.first_queue
        return top_element

    def empty(self):
        return len(self.first_queue) == 0


# -------------------- Queue using Stacks --------------------
class MyQueue(object):

    def __init__(self):
        self.first_stack = []
        self.second_stack = []

    def push(self, x):
        self.first_stack.append(x)

    def pop(self):
        if not self.second_stack:
            while self.first_stack:
                self.second_stack.append(self.first_stack.pop())
        return self.second_stack.pop()

    def peek(self):
        if not self.second_stack:
            while self.first_stack:
                self.second_stack.append(self.first_stack.pop())
        return self.second_stack[-1]

    def empty(self):
        return not self.first_stack and not self.second_stack