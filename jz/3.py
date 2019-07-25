class Node:
    def __init__(self, value, _next=None):
        self.value = value
        self._next = _next

# Stack
def printLinkedListFromTail(p):
    res = []
    res1 = []
    while p:
        res.append(p.value)
        p = p._next
    while res:
        res1.append(res.pop())
    return res1

# Recurse
def printLinkedListFromTail1(p, ret):
    if p._next:
        printLinkedListFromTail1(p._next, ret)
    ret.append(p.value)

if __name__ == '__main__':
    node1 = Node(1)
    node2 = Node(2)
    node3 = Node(3)
    node4 = Node(4)

    node1._next = node2
    node2._next = node3
    node3._next = node4
    head = node1

    print(printLinkedListFromTail(head))

    ret = []
    printLinkedListFromTail1(head, ret)
    print(ret)

