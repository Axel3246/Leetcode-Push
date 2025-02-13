class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        
        res = 0
        operators = ['+', '-', '*', '/']
        stack = []

        for token in tokens:
            if token in operators:
                print(f'Curr Token: {token}')
                i = int(stack.pop())
                j = int(stack.pop())
                if token == '+':
                    stack.append(str(i+j))
                elif token == '-':
                    stack.append(str(j-i))
                elif token == '*':
                    stack.append(str(i*j))
                else:
                    stack.append(str(int(j/i)))
                    #if floor(j/i) <= 0:
                     #   stack.append(str(ceil(j/i)))
                    #else:
                     #   stack.append(str(floor(j/i)))
            else:
                stack.append(token)
            #print(stack)
        
        #print(f'Final stack: {stack}')
        return int(stack.pop())