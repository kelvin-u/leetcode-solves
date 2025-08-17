from collections import deque

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def kSmallest(self, root, k):
        # bfs and then sort output arr into returning k smallest
        if not root:
            return []
        k_index = [k-1]
        
        q = deque()
        q.append(root)
        output = []
        
        while q:
            node = q.popleft()
            output.append(node.val)
            
            if node.left:
                q.append(node.left)
            if node.right:
                q.append(node.right)
        sorted_nodes = sorted(output)
        
        return sorted_nodes[k]
    
    def dfsK(self, root, k):
        output = []
        k_index = [k-1]
        def dfs(node):
            if not node:
                return node
            output.append(node.val)
            
            dfs(node.left)
            dfs(node.right)
            return output
        array = dfs(root)
        sorted_arr = sorted(array)
        return sorted_arr[k]
    def actualK(self, root, k):
        output = []
        def dfs(node):
            if not node:
                return node

            dfs(node.left)
            output.append(node.val)
            dfs(node.right)

        dfs(root)
        return output[k-1]
    def saveMem(self, root, k):
        count = 0
        result = None
        def dfs(node):
            nonlocal count, result
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
        

root = TreeNode(3)
root.left = TreeNode(1)
root.right = TreeNode(4)
root.left.right = TreeNode(2)

sol = Solution()
print(sol.saveMem(root, k=1))
