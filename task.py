from collections import deque
class MyStack(object):

    def __init__(self):
        self.first_queue = deque()
        self.second_queue = deque()

    def push(self, x):
        """
        :type x: int
        :rtype: None
        """
        self.first_queue.append(x)
        

    def pop(self):
        """
        Removes the element on the top of the stack and returns it.
        :rtype: int
        """
        while len(self.first_queue) > 1:
            self.second_queue.append(self.first_queue.popleft())
        top_element = self.first_queue.popleft()
        self.first_queue, self.second_queue = self.second_queue, self.first_queue        
        return top_element

    def top(self):
        """
        Returns the element on the top of the stack.
        :rtype: int
        """
        while len(self.first_queue) > 1:
            self.second_queue.append(self.first_queue.popleft())        
        top_element = self.first_queue[0]        
        self.second_queue.append(self.first_queue.popleft())
        self.first_queue, self.second_queue = self.second_queue, self.first_queue
        return top_element

    def empty(self):
        """
        :rtype: bool
        """
        return len(self.first_queue) == 0


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()