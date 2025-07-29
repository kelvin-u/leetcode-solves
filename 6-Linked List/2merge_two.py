l1 = [1, 2, 4]
l2 = [1, 3, 4]


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = None


def print_list(head):
    current = head
    while current:
        print(current.val, end="->")
        current = current.next
    print("None")
    return None


def reverse_ll(head):
    current = head
    previous = None

    while current:
        next_node = current.next
        current.next = previous
        previous = current
        current = next_node
    return previous


def list_to_ll(arr):
    dummy = ListNode()
    start = dummy

    for n in arr:
        start.next = ListNode(n)
        start = start.next
    return dummy.next


def merge_two_lists(l1, l2):
    dummy = ListNode()
    start = dummy

    while l1 and l2:
        if l1.val < l2.val:
            start.next = l1
            l1 = l1.next
        else:
            start.next = l2
            l2 = l2.next
        start = start.next

    if l1:
        start.next = l1
    elif l2:
        start.next = l2
    return dummy.next


arr1 = [1, 2, 3]
arr2 = [2, 3, 5]

l1 = list_to_ll(arr1)
l2 = list_to_ll(arr2)

two_lists = merge_two_lists(l1, l2)

print_list(two_lists)


list1 = [1, 2, 3] 
list2 = []

dummy = ListNode()
start = dummy

while list1 and list2:
    if list1.val < list2.val:
        start.next = list1
        list1 = list1.next
    else:
        start.next = list2
        list2 = list.next
    start = start,next
if list1:
    start.next = list1
if list2:
    pass
print stat.nwxt