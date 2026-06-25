class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []

        for ch in tokens:
            if ch == '+' or ch == '-' or ch =='/' or ch =='*':
                op1 = int(stack.pop())
                op2 = int(stack.pop())
                exp = 0
                match ch:
                    case '+':
                        exp = op2 + op1
                    case '-':
                        exp = op2 - op1
                    case '*':
                        exp = op2 * op1
                    case '/':
                        exp = int(op2 / op1)
                
                stack.append(exp)
                continue
            else:
                stack.append(int(ch))
                
        if stack:
            res = stack.pop()
            return res
        else:
            return 0
                

