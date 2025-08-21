nums = [1, 2, 3]


def subsets(nums):
    output = []
    subsets = []

    def dfs(i):
        if i == len(nums):  # base case
            output.append(subsets[:])
            return

        # yes path
        subsets.append(nums[i])
        dfs(i + 1)

        # no path
        subsets.pop()
        dfs(i + 1)

    dfs(0)
    return output

