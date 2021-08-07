class StackArray:
    def __init__(self):
        self._data = []

    def __len__(self):
        return len(self._data)

    def isempty(self):
        return len(self._data) == 0

    def push(self,e):
        self._data.append(e)

    def pop(self) :
        if self.isempty():
            print('stack is empty')
            return
        return self._data.pop()

    def top(self):
        if self.isempty():
            print('Stack is empty')
            return
        return self._data[-1]


s = StackArray()
s.push(5)
s.push(3)
print(s._data)
print('Length : ',len(s ))
print(s.pop())
print(s.isempty)
print(s.pop())
print(s.isempty())
s.push(7)
s.push(9) 
s.push(4)
print(s._data)
print(s.top())
print(s._data)