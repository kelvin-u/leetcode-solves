class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = None


def print_ll(head):
    current = head
    while current:
        print(current.val, end="->")
        current = current.next
    print("None")


def list_to_ll(arr):
    dummy = ListNode()
    start = dummy

    for n in arr:
        start.next = ListNode(n)
        start = start.next
    print_ll(dummy.next)


node1 = ListNode(1)
node2 = ListNode(2)
node3 = ListNode(3)



arr = [3, 2, 0, -4]



node1.next = node2
node2.next = node3
node3.next = node1
head = node1


def hasCycle(head):
    slow = head
    fast = head

    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        if slow == fast:
            return True
    return False


print(hasCycle(head))
