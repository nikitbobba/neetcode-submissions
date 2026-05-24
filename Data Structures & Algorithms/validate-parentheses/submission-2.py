class Solution:
    def isValid(self, s: str) -> bool:
        closeBracket = {
            '[': ']',
            '{': '}',
            '(': ')'
        }

        other = {
            ']': '[',
            ')': '(',
            '}': '{'
        }

 
        stack = []
        for c in s:
            print(stack)
            if c in closeBracket:
                stack.append(c)
                
            
            else:
                close = other[c]
                if len(stack) == 0:
                    return False
                
                val = stack.pop()
                if val == close:
                    continue
                else:
                    return False

        if len(stack) != 0:
            return False
        return True
        