# Stack Class implemented using Python Lists
class Stack:
    def __init__(self):
        self.items = []

    def __str__(self):
        return f"Stack: {str(tuple(self.items))}"

    def is_empty(self):
        return self.items == []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def peek(self):
        return self.items[len(self.items)-1]

    def size(self):
        return len(self.items)