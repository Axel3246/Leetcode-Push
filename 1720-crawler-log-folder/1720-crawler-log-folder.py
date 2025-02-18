class Solution:
    def minOperations(self, logs: List[str]) -> int:
        
        # Create a stack and an array containing the string 'operations'
        stack = []
        noappend = ['../', './']

        # Traverse through logs
        for log in logs:
            if stack: # If there's a stack, we are in a folder. Check for operation and act accordingly
                if log == '../':
                    stack.pop()
                elif log == './':
                    pass
                else:
                    stack.append(log)
            else:
                if log not in noappend: # Else, we don't have a stack, we need to append something, but we need to check if its not an operation
                    stack.append(log)

        return len(stack) # We return the lenght of the stack, since its the number of folders we need to go back