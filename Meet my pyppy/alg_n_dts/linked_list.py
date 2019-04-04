class Node:
    def __init__(self, val=None):
        self.value = val
        self.next_node = None

    @property
    def data(self):
        return self.value

    @data.setter
    def data(self, value):
        self.value = value

    @property
    def next(self):
        return self.next_node

    @next.setter
    def next(self, next_node):
        self.next_node = next_node


class LinkedList:
    def __init__(self):
        self.head = None

    def is_empty(self):
        return self.head is None

    def add_node(self, item):
        new_node = Node(item)
        new_node.next = self.head
        self.head = new_node

    def size(self):
        count = 0
        curr = self.head

        while curr is not None:
            count += 1
            curr = curr.next

        return count

    def search(self, item):
        curr = self.head

        found = False
        while curr is not None:
            if curr.data == item:
                found = True
                break
            else:
                curr = curr.next

        return found

    def remove(self, item):
        curr = self.head
        previous = None
        found = False

        while curr is not None and not found:
            if curr.data == item:
                found = True
            else:
                previous = curr

            if found:
                if previous is None:
                    self.head = curr.next
                else:
                    previous.next = curr.next
            else:
                raise ValueError('Value not found.')

    def insert(self, position, item):
        if position > self.size() - 1:
            raise IndexError('Index out of bounds.')

        node = Node(item)
        curr = self.head
        prev = self.head
        curr_pos = 0

        while curr is not None and curr_pos != position:
            prev = curr
            curr = curr.next
            curr_pos += 1
        prev.next = node
        node.next = curr

    def index(self, item):
        curr = self.head
        position = 0

        while curr is not None and curr.data != item:
            curr = curr.next
            position += 1

        return position

    def print_list(self):
        curr = self.head

        while curr is not None:
            print(curr.data)
            curr = curr.next


li = LinkedList()
li.add_node(1)
li.add_node(2)
li.add_node(3)
li.add_node(4)
li.print_list()


