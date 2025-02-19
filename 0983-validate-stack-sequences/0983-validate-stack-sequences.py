class Solution:
    def validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:
        
        stack = []
        i, j = 0, 0 
        flag = True

        while j != len(popped):
            # 1. Check if stack exist
            if stack:
                # 2. First, lets iterate through pushed. With this, we can properly populate the stack with the actions
                if i != len(pushed):
                    # 3. Check if stack[-1] is not equal to popped[j], so we can append and move to next index
                    if stack[-1] != popped[j]:
                        stack.append(pushed[i])
                        i += 1
                    # 4. If its equal, just pop and move index j
                    elif stack[-1] == popped[j]:
                        stack.pop()
                        j += 1
                # 5. If we are at the end of the append, it means we only care about the pops
                else:
                    # 6. So, we just check if the digits match. If yes, pop and move pointer j. If not, its false.
                    if stack[-1] == popped[j]:
                        stack.pop()
                        j += 1
                    else:
                        return False
            else:
                stack.append(pushed[i])
                i += 1

        # 7. If we manage to go through all actions, we return True
        return True
                

            