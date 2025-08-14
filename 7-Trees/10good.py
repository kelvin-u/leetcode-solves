class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def goodNodes(self, root):
        def dfs(node, max_val):
            count = 0
            if not node:
                return 0
            print(node.val)
            if node.val >= max_val:
                count += 1

            # update max val
            max_val = max(max_val, node.val)

            count += dfs(node.left, max_val)
            count += dfs(node.right, max_val)
            return count

        return dfs(root, root.val)


root = TreeNode(3)
root.left = TreeNode(1)
root.right = TreeNode(4)

root.left.left = TreeNode(3)

root.right.left = TreeNode(1)
root.right.right = TreeNode(5)

sol = Solution()

print(sol.goodNodes(root))
