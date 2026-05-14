class Solution:
    def checkValidString(self, s: str) -> bool:
        open_stack = []
        star_stack = []


        for i, char in enumerate(s):

            if char == "(":
                open_stack.append(i)
            elif char == "*":
                star_stack.append(i)
            elif char == ")":
                if open_stack:
                    open_stack.pop()
                    continue
                elif star_stack:
                    star_stack.pop()
                    continue
                else:
                    return False

        while open_stack and star_stack:
            open_idx = open_stack.pop()
            star_idx = star_stack.pop()
            
            if open_idx > star_idx:
                return False
        
        return len(open_stack) == 0
