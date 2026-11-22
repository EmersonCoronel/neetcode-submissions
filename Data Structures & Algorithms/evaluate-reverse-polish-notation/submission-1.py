class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        index = 0
        while index < len(tokens):
            num = tokens[index]
            if num in "+-*/":
                second = int(stack.pop())
                first = int(stack.pop())
                if num == "+":
                    stack.append(first + second)
                elif num == "-":
                    stack.append(first - second)
                elif num == "*":
                    stack.append(first * second)
                else:
                    stack.append(int(first / second))
            else:
                stack.append(int(num))
            index += 1
        return stack[0]