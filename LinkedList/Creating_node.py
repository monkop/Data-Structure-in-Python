class _Node:
    __slots__ = '_element', '_next'

    def __init__(self,element,next):
        self._element = element
        self._next = next

n1 = _Node(7, None)
n2 = _Node(4,None)
n3 = _Node(12,None)
n4 = _Node(8,None)
n5 = _Node(3,None)

n1._element
n1._next
n2._element
n2._next
n3._element
n3._next
n4._element
n4._next
n5._element
n5._next
print(n1._element,n1._next)
print(n2._element,n2._next)
print(n3._element,n3._next)
print(n4._element,n4._next)
print(n5._element,n5._next)