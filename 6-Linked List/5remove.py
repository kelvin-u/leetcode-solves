class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def arr_to_ll(arr):
    dummy = ListNode()
    start = dummy

    for n in arr:
        start.next = ListNode(n)
        start = start.next
    print(None)

    current = dummy.next
    while current:
        print(current.val, end="->")
        current = current.next
    print("None")


def removeNthFromEnd(head, n):
    dummy = ListNode()
    dummy.next = head

    fast = dummy
    slow = dummy

    for _ in range(n+1):
        fast = fast.next

    while fast:
        slow = slow.next
        fast = fast.next

    slow.next = slow.next.next
    return dummy.next
