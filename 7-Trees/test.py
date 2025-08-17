def validBST(root):

    def dfs(node, low, high):
        if not node:
            return True

        if not (low < node.val < high):
            return False

        return dfs(root.left, low, node.val) and dfs(root.right, node.val, high)

    return dfs(root, float("-inf"), float("inf"))

def kSmall(root, k):
    # output = []
    count = 0
    result = None
    # in order dfs
    def dfs(node):
        if not node or result:
            return node
        dfs(node.left)
        count += 1
        if count == k:
            result = node.val
            return 
        dfs(node.right)
    dfs(root)
    return result
        
