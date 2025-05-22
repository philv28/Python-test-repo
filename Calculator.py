import operator

# Supported operations
ops = {
    "+": operator.add,
    "-": operator.sub,
    "*": operator.mul,
    "/": operator.truediv
}

def calculate(expression):
    if expression.lower() == "exit":
        print("Exiting program...")
        exit()
    try:
        parts = expression.split()
        if len(parts) != 3 and expression.lower() != "exit":
            return "Invalid input format. Use: number operator number (e.g., 5 + 5)"
        
        num1, op, num2 = parts
        num1, num2 = float(num1), float(num2)
        
        if op in ops:
            return ops[op](num1, num2)
        else:
            return "Unsupported operation. Use +, -, *, or /"
    
    except ValueError:
        return "Invalid numbers. Please enter numeric values."

# Example usage
expression = input("Enter calculation (e.g., 5 + 5): ")
result = calculate(expression)
print("Result:", result)
