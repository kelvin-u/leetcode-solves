def validBST(root):

    def dfs(node, low, high):
        if not node:
            return True

        if not (low < node.val < high):
            return False

        return dfs(root.left, low, node.val) and dfs(root.right, node.val, high)

    return dfs(root, float("-inf"), float("inf"))

