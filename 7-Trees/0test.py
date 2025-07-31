class TreeNode:
    def __init__(self, data):
        self.data = data

        self.left = None
        self.right = None


root = TreeNode("R")
node_A = TreeNode("1")
node_B = TreeNode("2")


root.left = node_A
root.right = node_B

print(root.right.data)
