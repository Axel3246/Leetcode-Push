class Solution:
    def makeGood(self, s: str) -> str:
        
        stack = []
        
        for char in s:
            if stack:
                # CASE 1: Minus before mayus
                if char.isupper() and stack[-1] == char.lower():
                    stack.pop()
                # CASE 2: Mayus before minus
                elif char.islower() and stack[-1] == char.upper():
                    stack.pop()
                # CASE 3: No condition above is met
                else:
                    stack.append(char)
            # Append something to the stack first
            else:
                stack.append(char)

        print(stack)
        return ''.join(stack)
