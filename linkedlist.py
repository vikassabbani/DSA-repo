from exception import Empty


class linkedlist:

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

    def addfirst(self, e):
        newNode = self._Node(e, None)
        if self._isempty():
            self._head = newNode
            self._tail = newNode
        else:
            newNode._next = self._head
        self._head = newNode
        self._size += 1

    def addlast(self, e):
        newnode = self._Node(e, None)
        if self._isempty():
            self._head = newnode
            self._tail = newnode
        else:
            self._tail._next = newnode
        self._tail = newnode
        self._size += 1

    def addany(self, e, pos):
        newnode = self._Node(e, None)
        thead = self._head
        i = 1
        while i < pos:
            thead = thead._next
            i = i + 1
        newnode._next = thead._next
        thead._next = newnode
        self._size += 1

    def removefirst(self):
        if self._isempty():
            raise Empty('linked list is empty')
        value = self._head._element
        self._head = self._head._next
        self._size -= 1
        if self._isempty():
            self._tail = None
        return value

    def removelast(self):
        if self._isempty():
            raise Empty('linked list is empty')
        i = 0
        thead = self._head
        while i < len(self)-2:
            thead = thead._next
            i += 1
        self._tail = thead
        thead = thead._next
        value = thead._element
        self._tail._next = None
        self._size -= 1
        return value

    def removeany(self, pos):
        if self._isempty():
            raise Empty('linked list is empty')
        thead = self._head
        i = 1
        while i < pos-1:
            thead = thead._next
            i += 1
        value = thead._next._element
        thead._next = thead._next._next
        self._size -= 1
        return value

    def removeduplicates(self):
        current = self._head
        while current._next:
            if current._element == current._next._element:
                current._next = current._next._next
                continue
            current = current._next
        return self._head


    def display(self):
        thead = self._head
        while thead:
            print(thead._element, "-->", end='')
            thead = thead._next
        print()


L = linkedlist()
L.addlast(30)
L.addlast(20)
L.addlast(20)
L.addlast(20)
L.addlast(40)
L.display()
L.removeduplicates()
L.display()
