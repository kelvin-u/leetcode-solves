class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def goodNodes(self, root):

        def dfs(node, max_val):
            if not node:
                return node

            if node.val >= max_val:
                good = 1
            else:
                good = 0
            
            max_val = max(max_val, node.val)

            left = dfs(node.left, max_val)
            right = dfs(node.right, max_val)
            return good + left + right

        return dfs(root, root.val)
