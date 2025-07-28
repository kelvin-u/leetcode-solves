class ListNode:
    def __init__(self, val=0, next=None, random=None):
        self.val = val
        self.next = None
        self.random = random

    def __repr__(self):
        return f"ListNode({self.val})"


def lst_to_ll(arr):
    dummy = ListNode()
    start = dummy
    for n in arr:
        start.next = ListNode(n)
        start = start.next

    head = dummy.next
    current = head

    while current:
        print(current.val, end="->")
        current = current.next
    print("None")
    return dummy.next


# head = [[7, None], [13, 0], [11, 4], [10, 2], [1, 0]]

head = lst_to_ll([1, 2, 3])

current = head
map = {}

# just loop through each element
while current:
    map[current] = ListNode(current.val)
    current = current.next

# 2nd pass is linking
