from typing import List


class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        ans = []
        n = len(digits)
        num_map = {
            '2': 'abc',
            '3': 'def',
            '4': 'ghi',
            '5': 'jkl',
            '6': 'mno',
            '7': 'pqrs',
            '8': 'tuv',
            '9': 'wxyz'
        }

        def backtrack(index: int, path: str):
            if index == n:
                ans.append(path)
                return
            for letter in num_map[digits[index]]:
                backtrack(index + 1, path + letter)

        if digits:
            backtrack(0, '')
        return ans
