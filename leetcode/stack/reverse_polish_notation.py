from collections import deque
from typing import List
import math

class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        ops = {
            "+": lambda a,b: a + b,
            "-": lambda a,b: a - b,
            "*": lambda a,b: a * b,
            "/": lambda a,b: math.trunc(a / b),
        }
        stack = deque()
        stack.append(tokens[0])
        stack.append(tokens[1])
        i = 2
        while (i < len(tokens)):
            if (tokens[i] in ["+", "-", "*", "/"]):
                left = int(stack.pop())
                right = int(stack.pop())
                accumulate = ops[tokens[i]](right, left)
                print(f"operation: {right} {tokens[i]} {left}")
                print(accumulate)
                # accumulate becomes next right
                stack.append(accumulate)
            else:
                stack.append(tokens[i])
            i += 1
        return stack.pop()

if __name__ == "__main__":

    tokens = ["10","6","9","3","+","-11","*","/","*","17","+","5","+"]
    solution = Solution()
    print(solution.evalRPN(tokens))