class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = None


def list_to_ll(arr):
    dummy = ListNode()
    start = dummy

    for n in arr:
        start.next = ListNode(n)
        start = start.next

    head = dummy.next
    while head:
        print(head.val, end="->")
        head = head.next
    print("None")
    return dummy.next


l1 = [4, 3]
l2 = [7, 0]

l1 = list_to_ll(l1)
l2 = list_to_ll(l2)

dummy = ListNode()
start = dummy
 
carry = 0 

while l1 or l2 or carry:
    v1 = l1.val if l1.val else 0
    v2 = l2.val if l2.val else 0
    
    value  = v1 + v2 + carry
    
    carry = value // 10
    value = value % 10


    start.next = ListNode(value)

    start = start.next
    l1 = l1.next if l1 else 0
    l2 = l2.next if l2 else 0


current = dummy.next
while current:
    print(current.val, end='->')
    current = current.next
