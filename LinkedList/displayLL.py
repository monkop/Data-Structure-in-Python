class _Node:
    __slots__ = '_element', '_next'

    def __init__(self,element,next):
        self._element = element
        self._next = next

class LinkList:
    def __init__(self):
        self._head = None
        self._tail = None
        self._size = 0


    def __len__(self) :
        return self._size

    def isempty(self):
        return self._size == 0

    def addlast(self,e):
        newest =_Node(e,None)
        if self.isempty():
            self._head = newest
        else:
            self._tail._next = newest
        self._tail = newest
        self._size += 1
    def addfirst(self,e):
        newest = _Node(e,None)
        if self.isempty():
            self._head = newest
            self._tail = newest
        else:
            newest._next = self._head
            self._head = newest
        self._size += 1

    def search(self, key):
        p = self._head
        index = 0
        while p:
            if p._element == key:
                return index
            p = p._next
            index += 1
        return -1

    def display(self):
        p = self._head
        while p:
            print(p._element,end = " ")
            p = p._next 
        print()

linklist = LinkList()
linklist.addlast(7)
linklist.addlast(4)
linklist.addlast(12)
linklist.display()
print("Size:",len(linklist))
linklist.addlast(8)
linklist.addlast(3)
linklist.display()
print("Size:",len(linklist))
sc = linklist.search(int(input("")))
print("Result :",sc)
linklist.addfirst(int(input("")))
linklist.display()
print("Size:",len(linklist))

