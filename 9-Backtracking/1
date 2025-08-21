class Solution:
    def subsets(self, nums):
        path = []
        output = []

        def dfs(i):
            # base case exit
            if i == len(nums):
                output.append(path[:])
                return

            # yes decision
            path.append(nums[i])
            dfs(i + 1)

            path.pop()
            dfs(i + 1)

        dfs(0)

        return output


nums = [1, 2, 3]

sol1 = Solution()
print(sol1.subsets(nums))
