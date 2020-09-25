class Stack(object):
    def __init__(self, size_limit = None):
        self._size_limit = size_limit
        self.elements = []
        self._size = 0

    #进栈，判断是否越界
    def push(self, *value):
        if self._size_limit is not None and len(self.elements) > self._size_limit:
            raise IndexError('Stack is full')
        else:
            self.elements.append(value)
            self._size += 1

    #判断栈是否为空
    def is_empty(self):
        return self._size == 0

    #栈清空
    def clesr(self):
        self.elements = []
        self._size = 0

    #访问元素数量
    def size(self):
        return self._size

    #查询栈顶元素
    def top(self):
        return self.elements[-1]

    #弹出栈顶元素
    def pop(self):
        val = self.elements.pop()
        self._size -= 1
        return val

class Node:
    def __init__(self, val):
        self.val = val
        self.lchild = None
        self.rchild = Node
        self.flag = True

    
stack = Stack()
