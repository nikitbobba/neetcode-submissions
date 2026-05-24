class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        brackets = {
            ')': '(',
            '}': '{',
            ']': '['
        }
        
        for c in s:
            # opening bracket
            if c in brackets.values():
                stack.append(c)
                continue
            
            # closing bracket
            if c in brackets.keys():
                if len(stack) == 0:
                    return False
                val = stack.pop()
                if val != brackets[c]:
                    return False
        
        if len(stack) != 0:
            return False

        return True