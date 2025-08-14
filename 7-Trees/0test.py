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


def rightSide(root):
    if not root:
        return []

    q = deque()
    q.append(root)
    output = []

    while q:
        q_len = len(q)
        num = q[-1]
        output.append(num.val)

        # adding nodes
        for _ in range(q_len):
            node = q.popleft()

            if node.left:
                q.append(node.left)
            if node.right:
                q.append(node.right)
    return output


print(rightSide(root))
