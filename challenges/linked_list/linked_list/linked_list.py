class Node:

    def __init__(self, value, next=None):
        self.value = value
        self.next = next


class LinkedList:

    def __init__(self, head, values=None):
        self.head = head

    def insert(self, value):
        node = Node(value) 

        if self.head is not None:
            node.next = self.head
        self.head = node
    
    def __str__():
        if LinkedList:
            return (f'{ a } -> { b } -> { c } -> NULL')