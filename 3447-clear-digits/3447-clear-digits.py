class Solution:
    def clearDigits(self, s: str) -> str:
        
        stack = []

        for d in s:
            if d.isdigit():
                if not stack[-1].isdigit():
                    stack.pop()
            else:
                stack.append(d)
        
        return ''.join(stack)