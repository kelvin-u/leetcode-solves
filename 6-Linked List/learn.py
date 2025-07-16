class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def print_list(self):
        current = self.head
        while current:
            print(current.data, end="->")
            current = current.next
        print("None")

    def list_count(self):
        current = self.head
        length = 0
        while current:
            current = current.next
            length += 1
        print(length)

    def reverseList(self, head):
        current = head
        previous = None

        while current is not None:
            next_node = current.next
            current.next = previous
            previous = current
            current = next_node
        return previous


node1 = Node(10)
node2 = Node(20)
node3 = Node(30)

node1.next = node2
node2.next = node3

ll = LinkedList()
ll.head = node1

ll.print_list()

ll.head = ll.reverseList(ll.head)
ll.print_list()
# print all the values
