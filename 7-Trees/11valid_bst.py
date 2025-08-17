class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isValidBST(self, root):
        def dfs(node, low, high):
            if not node:
                return True
            
            print(node.val)
            if not (low < node.val < high):
                print(node.val)
                return False

            return dfs(node.left, low, node.val) and dfs(node.right, node.val, high)

        return dfs(root, float("-inf"), float("inf"))


root = TreeNode(5)
root.left = TreeNode(1)
root.right = TreeNode(7)
root.right.left = TreeNode(6)
root.right.right = TreeNode(8)

sol = Solution()
print(sol.isValidBST(root))
