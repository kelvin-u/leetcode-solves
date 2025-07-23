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
    return dummy.next


arr = [1, 2, 3, 4, 5, 6]

head = list_to_ll(arr)


def hasCycle(head):
    slow = head
    fast = head

    count = 0
    
    # while current and next node arent none
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next

        count += 1
        print(count)
        if slow == fast:
            return True
    return False


print(hasCycle(head))
