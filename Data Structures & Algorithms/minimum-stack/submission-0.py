class MinStack:

    def __init__(self):
        self.stack = []
        self.stack2 = []
        Min = float('inf')

    def push(self, val: int) -> None:
        self.stack.append(val)
        if self.stack2:
            val = min(val, self.stack2[-1])
        self.stack2.append(val)

    def pop(self) -> None:
        self.stack.pop(-1)
        self.stack2.pop(-1)

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.stack2[-1]
        
