class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def kSmallest(self, root, k):
        count = 0
        result = None

        # in order traversal
        def dfs(node):
            nonlocal count
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

    def kOther(self, root, k):
        output = []

        def dfs(node):
            if not node:
                return node

            dfs(node.left)
            output.append(node.val)
            dfs(node.right)

        dfs(root)

        return output[k - 1]
