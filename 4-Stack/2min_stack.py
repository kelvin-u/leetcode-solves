class MinStack:

    def __init__(self):
        # two stacks
        self.stack = []
        self.minStack = []

    def push(self, val: int) -> None:
        self.stack.append(val)
        if self.minStack: # non empty
            self.minStack.append(min(val, self.minStack[-1]))
        else: # empty min stack 
            self.minStack.append(val)


    def pop(self) -> None:
        self.stack.pop()
        self.minStack.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.minStack[-1]