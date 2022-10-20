class Solution:
    def numsSameConsecDiff(self, n: int, k: int) -> List[int]:

        result = []

        def dfs(curr, times):
            if times == 0:
                result.append(curr)
                return

            tail = curr % 10
            next_ = set([tail + k, tail - k])
            for num in next_:
                if num >= 0 and num <= 9:
                    dfs(curr * 10 + num, times - 1)

        for i in range(1, 10):
            dfs(i, n - 1)

        return result