class Solution:
    def isHappy(self, n: int) -> bool:
        visited = set()


        while True:

            curr_ans = 0

            while n > 0:
                
                rem = n % 10
                curr_ans += (rem * rem)
                n = n // 10
                
            if curr_ans == 1:
                return True
            if curr_ans in visited:
                return False

            visited.add(curr_ans)
            n = curr_ans