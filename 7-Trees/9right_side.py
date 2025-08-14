from collections import deque


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def rightSideView(self, root):
        if not root:
            return []

        q = deque()
        q.append(root)
        output = []

        while q:
            q_length = len(q)
            right_num = q[-1]
            output.append(right_num.val)

            for _ in range(q_length):
                node = q.popleft()
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
        return output


node5 = TreeNode(5)
node4 = TreeNode(4)
node3 = TreeNode(3, None, node4)
node2 = TreeNode(2, None, node5)
root = TreeNode(1, node2, node3)

sol = Solution()
print(sol.rightSideView(root))
