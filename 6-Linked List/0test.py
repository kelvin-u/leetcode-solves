class Node:
    def __init__(self, val):
        self.val = val
        self.Next = None

def merge_lists(l1, l2):
    dummy = Node()
    start = dummy

    while l1 and l2:
        if l1.val < l2.val:
            start.next = l1
            l1 = l1.next
        else:
            start.next = l2
            l2 = l2.next
    
    # not edge case where != l1 = [1,2,3] l2 = [], remaining people bro attach the rest to the tail 
    if l1:
        start.next = l1
    elif l2:
        start.next = l2

    return dummy.next