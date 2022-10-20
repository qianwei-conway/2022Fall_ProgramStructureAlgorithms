class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:

        rows, cols = len(board), len(board[0])
        used = set()

        def dfs(r, c, index):

            if index == len(word):
                return True
            if r < 0 or r >= rows or c < 0 or c >= cols or board[r][c] != word[index] or (r, c) in used:
                return False

            used.add((r, c))
            res = dfs(r + 1, c, index + 1) or dfs(r - 1, c, index + 1) or dfs(r, c + 1, index + 1) or dfs(r, c - 1,
                                                                                                          index + 1)
            used.remove((r, c))

            return res

        for i in range(rows):
            for j in range(cols):
                if dfs(i, j, 0):
                    return True
        return False