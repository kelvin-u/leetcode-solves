class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isSubTree(root, subRoot):
        def isSame(p, q):
            if p is None and q is None:
                return True
            if p is None or q is None:
                return False
            if p.val != q.val:
                return False
            return isSame(p.left, q.left) and isSame(p.right, q.right)

        if subRoot is None:
            return True
        if root is None:
            return False
        return (
            isSame(root, subRoot)
            or isSame(root.left, subRoot)
            or isSame(root.right, subRoot)
        )
