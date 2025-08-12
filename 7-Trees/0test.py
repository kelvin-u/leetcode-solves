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


# root = []
def diameter(root):
    diameter = 0

    def depth(root):
        nonlocal diameter
        if not root:
            return 0
        left = depth(root.left)

        right = depth(root.right)
        print(f"Node {root.val}: left depth = {left}, right depth = {right}")

        diameter = max(diameter, left + right)

        return 1 + max(left, right)

    depth(root)
    return diameter


print
