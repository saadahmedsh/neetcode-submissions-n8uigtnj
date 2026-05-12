class Solution:
    def partition(self, s: str) -> List[List[str]]:

        res = []
        subset = []

        def is_palindrome(s, i, j):
            l = i
            r = j
            while l < r:
                if s[l] != s[r]:
                    return False
                l += 1
                r -= 1

            return True

        def dfs(i):
            if i >= len(s):
                res.append(subset.copy())
                return


            for j in range(i, len(s)):
                if is_palindrome(s, i, j):
                    subset.append(s[i: j + 1])
                    dfs(j + 1)
                    subset.pop()

        dfs(0)

        return res



        