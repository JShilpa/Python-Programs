class ArrayStack:
 pass

 def __init__(self):
    self._data = [];

 def __len__(self):
    return len(self._data);

 def push(self, e):
    self._data.append(e);

 def is_empty(self):
    return len(self._data) == 0;

 def pop(self):
    if self.is_empty():
        raise Empty("Stack is empty")
    else:
        return self._data.pop();

 def getitem(self):
     return self._data;