"""
Given a Stack S, write a python function to retrieve efficiently the maximum value inside S.
"""

class MaxStack:
    def __init__(self):
        self.stack = []
        self.max_stack = []

    def push(self, value):
        self.stack.append(value)
        if not self.max_stack or value >= self.max_stack[-1]:
            self.max_stack.append(value)

    def pop(self):
        if not self.stack:
            return None
        if self.stack[-1] == self.max_stack[-1]:
            self.max_stack.pop()
        return self.stack.pop()

    def max_value(self):
        return self.max_stack[-1] if self.max_stack else None


