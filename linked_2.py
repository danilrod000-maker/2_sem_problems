
class SList:
    pass
2


def prepend(lst, data):
    lst.head = lst.next
    lst.head = data
    return lst

def append(lst, data):
    if lst is None:
        return prepend(lst, data)

    current = lst.head
    while current.next:
        current = current.next

    current.next = data
    return lst



def length(lst): #ok
    count = 0
    current = lst.head
    while current:
        count += 1
        current = current.next

    return count

def get(lst, index):
    if index < 0:
        return None

    current = lst.head
    i = 0

    while current:
        if i == index:
            return current.data
        current = current.next
        i += 1


def get_last(lst):
    if lst is None:
        return None

    current = lst.head
    while current.next:
        current = current.next


    return current.data


def find(lst, data):
    if lst is None:
        return -1

    current = lst.head
    index = 0

    while current:
        if current.data == data:
            return index
        current = current.next
        index += 1

    return -1


# исправляй остальные
def remove_first(lst, data):
    if lst is None:
        return None

    if lst.head.data == data:
        lst.head = lst.head.next
        return lst

    prev = lst.head
    current = lst.head.next

    while current:
        if current.data == data:
            prev.next = current.next
            return lst
        prev = current
        current = current.next
def remove_all(lst, data):
    while lst is not None and lst.head.data == data:
        lst.head = lst.head.next

    if lst.head is None:
        return

    current = lst.head
    while current.nexte:
        if current.next.data == data:
            current.next = current.next.next
        else:
            current = current.next

def copy(lst):
    if lst is None:
        return None

    head = SList()
    head.data = lst.data
    head.next = None

    tail = head
    current = lst.next

    while current:
        node = SList()
        node.data = current.data
        node.next = None

        tail.next = node
        tail = node
        current = current.next
    return head

def concat(lst1, lst2):
    if lst1 is None:
        return copy(lst2) # чтобы старые не трогать

    head = copy(lst1)
    current = head
    while current.next:
        current = current.next

    current.next = copy(lst2)
    return head

def foreach(lst, func):
    current = lst
    while current:
        func(current.data)
        current = current.next

def find_custom(lst, predicate):
    current = lst
    index = 0

    while current:
        if predicate(current.data):
            return current.data, index
        current = current.next
        index += 1
    return None, -1

def from_list(lst):
    head = None
    for item in reversed(lst):
        head = prepend(head, item)
    return head

def to_list(lst):
    result = []
    current = lst

    while current:
        result.append(current.data)
        current = current.next
    return result


# тесты чере полчасика будут обязательно!!!



#проверки с None
# убрать head
# lst  -начало
# подумай про аппенд
