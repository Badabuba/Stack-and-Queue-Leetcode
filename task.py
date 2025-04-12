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


class FreqStack(object):
    def __init__(self):
        self.freq = {}
        self.group = {}
        self.maxfreq = 0

    def push(self, val):
        """
        :type val: int
        :rtype: None
        """
        if val in self.freq:
            self.freq[val] += 1
        else:
            self.freq[val] = 1
        f = self.freq[val]

        if f > self.maxfreq:
            self.maxfreq = f

        if f not in self.group:
            self.group[f] = deque()
        self.group[f].append(val)

    def pop(self):
        """
        :rtype: int
        """
        val = self.group[self.maxfreq].pop()
        self.freq[val] -= 1

        if not self.group[self.maxfreq]:
            del self.group[self.maxfreq]
            self.maxfreq -= 1

        return val