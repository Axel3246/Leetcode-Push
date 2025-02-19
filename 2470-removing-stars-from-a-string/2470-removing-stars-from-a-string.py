class Solution:
    def removeStars(self, s: str) -> str:
        
        stack = []

        for i in s:
            if stack:
                if i == '*':
                    stack.pop()
                else:
                    stack.append(i)
            else:
                stack.append(i)

        return ''.join(stack)