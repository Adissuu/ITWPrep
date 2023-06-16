# Min stack

## Design a stack that supports push, pop, top, and retrieving the minimum element in constant time.

```
# time complexity: O(1)
# space complexity: O(n)
class MinStack(object):
    def __init__(self):
        self.stack = []
        self.minStack = []

    def push(self, val):
        self.stack.append(val)
        val = min(val, self.minStack[-1] if self.minStack else val)
        self.minStack.append(val)

    def pop(self):
        self.stack.pop()
        self.minStack.pop()

    def top(self):
        return self.stack[-1]
        

    def getMin(self):
        return self.minStack[-1]
```

### By keeping a minimum value stack, it is easier to keep track of the minimum at all times, and therefore avoiding the search of the array for the minimum value.