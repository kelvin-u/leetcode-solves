# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def diameterOfBinaryTree(self, root):
        self.diameter = 0

        # use the depth of the left and right and add them

        def depth(root):
            if not root:
                return 0

            left = depth(root.left)
            right = depth(root.right)

            self.diameter = max(self.diameter, left + right)

            # this doesnt really have anything to do with this problem
            return 1 + max(left, right)

        depth(root)
        return self.diameter
