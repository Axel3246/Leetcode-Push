class Solution:
    def simplifyPath(self, path: str) -> str:
        
        stack = []
        idx = 0

        while idx != len(path):
            stackHelper = []
            print(f' stack is {stack}, char is {path[idx]}, idx is {idx}')

            # First check if stack exists
            if stack:

                # Case 1: Char is / and stack[-1] is not / (avoid duplicates)
                if path[idx] == '/':
                    if stack[-1] != '/':
                        stack.append(path[idx])
                    idx += 1

                # Case 2: Char is a '.', we need to count how many
                elif path[idx] == '.':
                    flag = False
                    while idx != len(path) and (path[idx] == '.' or path[idx] != '/'):
                        if path[idx].isalnum():
                            flag = True
                        stackHelper.append(path[idx])
                        idx += 1

                    # 2.1 Only one .
                    print(f'MI RUTA ES {stackHelper}')
                    print(stack[-1].isalnum())
                    if flag:
                        stack.append(''.join(stackHelper))
                    else:
                        if len(stackHelper) != 1:
                            if len(stackHelper) == 2:
                                if len(stack) == 1:
                                    stack.pop()
                                else:
                                    print('POPP')
                                    stack.pop()
                                    stack.pop()
                            else:
                                stack.append(''.join(stackHelper))
                            
                else:
                    while (idx != len(path) and path[idx].isalnum()) or (idx != len(path) and path[idx] != '/'):
                        stackHelper.append(path[idx])
                        idx += 1
                        #print(idx)

                    stack.append(''.join(stackHelper))
            else:
                stack.append(path[idx])
                idx += 1   
    

        #print(stack)
        #print(f"Final Stack: {''.join(stack)}")
        if len(stack) > 1:
            if stack[-1] == '/':
                stack.pop()
            return ''.join(stack)
        else:
            return '/'
      