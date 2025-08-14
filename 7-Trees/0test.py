from collections import deque


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


node5 = TreeNode(5)
node4 = TreeNode(4)
node3 = TreeNode(3)
node2 = TreeNode(2, node4, node5)
root = TreeNode(1, node2, node3)


def dfs(root):
    if not root:
        return root
    print(root.val)
    dfs(root.left)
    dfs(root.right)


def bfs(root):
    if not root:
        return
    q = deque()
    q.append(root)

    while q:
        node = q.popleft()
        print(node.val, end=" ")

        if node.left:
            q.append(node.left)
        if node.right:
            q.append(node.right)

        q_len = len(q)
        """for i in range(q_len): level traversal
            node = q.popleft()
            print(node.val)
            if node.left:
                q.append(node.left)
            if node.right:
                q.append(node.right)"""


print(bfs(root))
