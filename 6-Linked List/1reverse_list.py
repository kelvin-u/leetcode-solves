class LinkedList:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def reverseList(self, head):
        current = head
        previous = None
        while current:
            next_node = current.next
            current.next = previous
            previous = current
            current = next_node
        return previous

    def print_list(self):
        current = self
        while current:
            print(current.val, end="->")
            current = current.next
        print("None")
        return None


node1 = LinkedList(1)
node2 = LinkedList(2)
node3 = LinkedList(3)

node1.next = node2
node2.next = node3

head = node1

node1.print_list()
