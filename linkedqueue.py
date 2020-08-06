from exception import Empty

class linkedqueue:

    class _Node:
        __slots__ = '_element', '_next'

        def __init__(self, element, next):
            self._element = element
            self._next = next

    def __init__(self):
        self._head = None
        self._tail = None
        self._size = 0

    def __len__(self):
        return self._size

    def _isempty(self):
        return self._size == 0

    def enqueue(self, e):
        newNode = self._Node(e, None)
        if self._isempty():
            self._head = newNode
        else:
            self._tail._next = newNode
        self._tail = newNode
        self._size += 1

    def dequeue(self):
        if self._isempty():
            raise Empty('linked list is empty')
        value = self._head._element
        self._head = self._head._next
        self._size -= 1
        if self._isempty():
            self._tail = None
        return value

    def display(self):
        thead = self._head
        while thead:
            print(thead._element, "-->", end='')
            thead = thead._next
        print()


L = linkedqueue()
