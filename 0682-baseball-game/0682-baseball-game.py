class Solution:
    def calPoints(self, operations: List[str]) -> int:
        
        stack = []
        

        for op in operations:
            if op == 'C':
                stack.pop()
            elif op == '+':
                one = int(stack.pop())
                two = int(stack.pop())
                stack.append(two)
                stack.append(one)
                stack.append(two+one)
            elif op == 'D':
                stack.append(stack[-1]*2)
            else:
                stack.append(int(op))

        return sum(stack)