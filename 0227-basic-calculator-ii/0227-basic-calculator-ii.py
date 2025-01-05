class Solution:
    def calculate(self, s: str) -> int:
        """
        Summary:
            Evaluate the expression.
            Assume the expression is always valid.
            All intermediate results will be in the range of [-2^31, 2^31-1].
        Args:
            (str) s which represents an expression
                s consists of integers and operators
                 ('+', '-', '*', '/') separated by some number of spaces.
        Returns:
            Evaluated value.
        """
        # Stores the closest number encountered. 
        # Therefore, is the right operand.
        num = 0

        # previous operator that we have encountered.
        pre_op = '+'

        # To allow processing the last pre_op in the stack.
        # In fact, any one of +-*/ works.
        s += '+'
        stack = []

        for c in s:
            # Handle multi-digit numbers.
            if c.isdigit():
                num = num * 10 + int(c)
            # Ignore whitespaces.
            elif c == ' ':
                continue
            # c is an operator in +-*/
            else:
                if pre_op == '+':
                    stack.append(num)
                elif pre_op == '-':
                    stack.append(-num)
                # * and / has priority over + and -.
                # So directly calculate their result and add to stack.
                elif pre_op == '*':
                    operand = stack.pop()
                    # Push evaluated value to stack.
                    stack.append(operand * num)
                elif pre_op == '/':
                    operand = stack.pop()
                    # Round division result to integer closest to zero.
                    stack.append(int(operand / num))
                # reset operand number to 0
                num = 0
                # Update operator that we have encountered that we should work with.
                pre_op = c
        # stack is left with integers to add together.
        return sum(stack)