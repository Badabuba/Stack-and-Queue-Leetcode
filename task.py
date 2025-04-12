class MyQueue(object):

    def __init__(self):
        self.first_stack = []
        self.second_stack = []

    def push(self, x):
        """
        :type x: int
        :rtype: None
        """
        self.first_stack.append(x)
        

    def pop(self):
        """
        :rtype: int
        """
        if not self.second_stack:
            while self.first_stack:
                self.second_stack.append(self.first_stack.pop())
        return self.second_stack.pop()

    def peek(self):
        """
        :rtype: int
        """
        if not self.second_stack:
            while self.first_stack:
                self.second_stack.append(self.first_stack.pop())
        return self.second_stack[-1]

    def empty(self):
        """
        :rtype: bool
        """
        return not self.first_stack and not self.second_stack


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()