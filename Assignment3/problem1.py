class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:

        candidates.sort()
        res = []

        def backtrack(remain, sub_res, start):

            if remain > 0:
                for i in range(start, len(candidates)):
                    sub_res.append(candidates[i])
                    backtrack(remain - candidates[i], sub_res, i)
                    sub_res.pop()
            elif remain == 0:
                res.append(sub_res.copy())
            return

        backtrack(target, [], 0)
        return res