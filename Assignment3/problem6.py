class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        result = []

        sub_res = []

        def dfs(index):
            if index >= len(nums):
                result.append(sub_res.copy())
                return

            # include the nums[index]
            sub_res.append(nums[index])
            dfs(index + 1)

            # not include the nums[index]
            sub_res.pop()
            dfs(index + 1)

        dfs(0)
        return result