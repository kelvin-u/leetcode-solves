class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def goodNodes(self, root):
        def dfs(node, max_val):
            ount = 0
            if not node:
                return 0
            if node.val >= max_val:
                count += 1
            
            # update max val
            max_val = max(max_val, node.val)
            
            count += dfs(node.left, max_val)
            count += dfs(node.right, max_val)
            return count
        return dfs(root, root.val)
