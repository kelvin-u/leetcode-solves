class Solution:
    def combinationSum(self, candiadates, target):
        output = []

        def dfs(i, path, total):
            if i == target:
                output.append(path[:])
                return
            if i == len(candiadates) or total > target:
                return

            path.append(candiadates[i])
            dfs(i + 1, path, total + candiadates[i])

            path.pop()
            dfs(i, path, total)

        dfs(0, [], 0)
        return output
