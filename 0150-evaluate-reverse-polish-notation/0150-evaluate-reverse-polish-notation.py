class Solution:
    def evalRPN(self, tokens: list[str]) -> int:
        # 1. Define explicit, named functions for each operation
        def add(a, b):
            return a + b
            
        def subtract(a, b):
            return a - b
            
        def multiply(a, b):
            return a * b
            
        def divide(a, b):
            return int(a / b)  # Forces truncation toward zero
            
        # 2. Map the symbols to the function names. 
        # Notice there are NO parentheses after the function names!
        operations = {
            "+": add,
            "-": subtract,
            "*": multiply,
            "/": divide
        }
        
        stack = []
        
        for token in tokens:
            if token in operations:
                # Pop right then left
                right_num = stack.pop()
                left_num = stack.pop()
                
                # Grab the correct function from the dictionary
                math_func = operations[token]
                
                # Execute it with our numbers
                result = math_func(left_num, right_num)
                
                stack.append(result)
            else:
                # If it's not a math symbol, it must be a number
                stack.append(int(token))
                
        return stack[0]