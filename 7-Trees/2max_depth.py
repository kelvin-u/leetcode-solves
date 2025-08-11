# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def maxDepth(self, root):
        if not root:
            return 0
        left = self.maxDepth(root.left)
        right = self.maxDepth(root.right)
        return 1 + max(left, right)


node7 = TreeNode(7)
node15 = TreeNode(15)
node20 = TreeNode(20, node15, node7)
node9 = TreeNode(9)
root = TreeNode(3, node9, node20)

sol = Solution()

test = sol.maxDepth(root)
    
print(test)