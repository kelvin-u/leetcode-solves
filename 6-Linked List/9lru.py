class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value

        self.next = None
        self.prev = None


class LRUCache:
    def __init__(self, capacity):
        self.capacity = capacity
        self.cache = {}

        self.left = Node(0, 0)
        self.right = Node(0, 0)
        self.left.next = self.right
        self.right.prev = self.left

    def remove(self, node):
        prev_node = node.prev
        next_node = node.next

        prev_node.next = next_node
        next_node.prev = prev_node

    def insert(self, node):
        prev_node = self.right.prev
        next_node = self.right

        prev_node.next = node
        next_node.prev = node

        node.next = next_node
        node.prev = prev_node

    def get(self, key):
        # get(1)
        if key in self.cache:
            self.remove(self.cache[key])
            self.insert(self.cache[key])
            return self.cache[key].value
        return -1

    def put(self, key, value):
        # put(3,3)
        if key in self.cache:
            self.remove(self.cache[key])
        self.cache[key] = Node(key, value)
        self.insert(self.cache[key])

        if len(self.cache) > self.capacity:
            # remove lru
            lru = self.left.next
            self.remove(lru)
            del self.cache[lru.key]
