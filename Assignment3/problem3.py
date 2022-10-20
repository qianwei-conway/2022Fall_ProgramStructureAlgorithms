class Solution:
    def letterCombinations(self, digits: str) -> List[str]:

        num_letter = {'2': 'abc', '3': 'def', '4': 'ghi', '5': 'jkl', '6': 'mno', '7': 'pqrs', '8': 'tuv', '9': 'wxyz'}

        def combine(index, string):

            if len(string) == len(digits):
                res.append(string)
                return

            for char in num_letter[digits[index]]:
                string += char
                combine(index + 1, string)
                string = string[:-1]

        res = []
        if len(digits) == 0:
            return res

        combine(0, '')
        return res