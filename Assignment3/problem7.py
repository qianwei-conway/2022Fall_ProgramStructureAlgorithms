class Solution:
    def generateParenthesis(self, n: int) -> List[str]:

        result = []
        sub_res = ''

        def dfs(openN, closeN):
            nonlocal sub_res
            if openN == closeN == n:
                result.append(sub_res)
                return

            if openN < n:
                sub_res += '('
                dfs(openN + 1, closeN)
                sub_res = sub_res[:-1]

            if closeN < openN:
                sub_res += ')'
                dfs(openN, closeN + 1)
                sub_res = sub_res[:-1]

        dfs(0, 0)
        return result