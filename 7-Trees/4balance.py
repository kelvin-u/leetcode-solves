class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isBalanced(self, root):
        # get the depth of the left and right
        def dfs(root):
            if not root:
                return [True, 0]
            left = dfs(root.left)
            right = dfs(root.right)

            bal = left[0] and right[0] and abs(left[1] - left[1]) <= 1

            return [bal, 1 + max(left[1], right[1])]

        output = dfs(root)
        return output[0]


node7 = TreeNode(7)
node15 = TreeNode(15)
node20 = TreeNode(20, node15, node7)
node9 = TreeNode(9)
root = TreeNode(3, node9, node20)

sol = Solution()
print(sol.isBalanced(root))
