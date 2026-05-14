class Node:
    pass

class LinkedList:
    pass



def create_node(data):
    node = Node()
    node.data = data
    node.next = None
    return node


def create_list():
    lst = LinkedList()
    lst.head = None
    return lst


def append(lst, data):
    # cоздаем новый узел
    new_node = create_node(data)
    # путстой
    if lst.head is None:
        lst.head = new_node
        return

    current = lst.head
    while current.next is not None:
        current = current.next

    current.next = new_node

def prepend(lst, data):
    new_node = create_node(data)
    new_node.next = lst.head
    lst.head = new_node


