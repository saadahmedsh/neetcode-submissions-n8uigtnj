class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []

        res = []
        

        digitToChar = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "qprs",
            "8": "tuv",
            "9": "wxyz",
        }


        def backtrack(i, curr_str):
            if len(curr_str) == len(digits):
                res.append(curr_str)
                return

            characters = digitToChar[digits[i]]
            for c in characters:
                backtrack(i + 1, curr_str + c)


        backtrack(0, "")
        return res


