# LeetCode 155 - Min Stack
# Difficulty: Medium
# Topic: Stack, Design
# Time Complexity: O(1)
# Space Complexity: O(n)

class MinStack(object):

    def __init__(self):
        self.stack = []
        self.minStack = []
        

    def push(self, val):
        self.stack.append(val)
        if not self.minStack or val <= self.minStack[-1]:
            self.minStack.append(val)

    def pop(self):
        a = self.stack.pop()
        if a == self.minStack[-1]:
            return self.minStack.pop()
        return a

    def top(self):
        return self.stack[-1]
        

    def getMin(self):
        return self.minStack[-1]
        

# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()