class Stack():
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        #pop method removes top element in stack and actually returns the popped element too
        return self.items.pop()

    def is_empty(self):
        #returns boolean value of if stack is empty or not
        return self.items == []

    def peek(self):
        #returns element at top of stack, if empty returns null
        if self.is_empty() == false:
            return self.items[-1]

    def size(self):
        return len(self.items)

    def search(self, item):
        #returns the position of the element if it is successfully found in the stack (taking the count as base 1)
        for i in range(len(self.items)):
            if self.items[i] == item:
                return i + 1
        return -1

    def print_stack(self):
        return print(self.items)
