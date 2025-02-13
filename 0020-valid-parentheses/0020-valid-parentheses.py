class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        #1. Create an stack and an opening
        stack = []
        opening = ["(", '[', '{']
        mapp = {')':'(', ']':'[', '}':'{'}
        #2. Loop through the string
        for c in s:
            #3. If c is an opening parenthesis append
            if c in opening:
                stack.append(c)
            else:
                # 4. Else, if there is something in the stack, try the following
                if stack and stack[-1] == mapp[c]:
                        stack.pop()
                else:
                    # If theres nothing and we encounter a closing brace, false
                    return False
        
        # If theres something in the stack, return False (missing braces), else return True
        return not stack
        