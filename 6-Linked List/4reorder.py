class ListNode:

    def __init__(self, val=0, next=None):
        self.val = val
        self.next = None


def list_prt(head):
    current = head
    while current:
        print(current.val, end="->")
        current = current.next
    print("none")


def arr_to_list(arr):
    dummy = ListNode()
    start = dummy

    for n in arr:
        start.next = ListNode(n)
        start = start.next
    list_prt(dummy.next)


arr = [1, 2, 3, 4]

# 1 -> 2 -> 3 -> 4 -> NULL


def reorderList(head):
    # find the mid point 

    slow = head
    fast = head

    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
    
    current = slow.next
    previous = None

    while current:
        next_node = current.next
        current.next = previous
        previous = current
        current = next_node
    slow.next = None

    # merging
    head1 = head
    head2 = previous

    while head2:
        tmp1 = head1.next
        tmp2 = head2.next

        head1.next = head2
        head2.next = tmp1

        head1.next = tmp1
        head2.next = tmp2
    


arr_to_list(arr)


