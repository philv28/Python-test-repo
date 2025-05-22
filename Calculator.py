# Import the operator module which provides basic arithmetic operations
import operator

# Dictionary mapping operator symbols to their corresponding functions from the operator module
ops = {
    "+": operator.add,  # Addition operation
    "-": operator.sub,  # Subtraction operation
    "*": operator.mul,  # Multiplication operation
    "/": operator.truediv  # Division operation
}

def calculate(expression):
    """
    Process a mathematical expression and return the result.
    
    Args:
        expression (str): A string containing two numbers and an operator separated by spaces
                         Example: "5 + 3" or "10 * 2"
    
    Returns:
        float: The result of the calculation
        str: Error message if the input is invalid
    """
    # Check if user wants to exit the program
    if expression.lower() == "exit":
        print("Exiting program...")
        exit()
        
    try:
        # Split the expression into parts (number, operator, number)
        parts = expression.split()
        
        # Validate input format
        if len(parts) != 3 and expression.lower() != "exit":
            return "Invalid input format. Use: number operator number (e.g., 5 + 5)"
        
        # Unpack the parts into variables
        num1, op, num2 = parts
        
        # Convert string numbers to float type
        num1, num2 = float(num1), float(num2)
        
        # Check if the operator is supported and perform calculation
        if op in ops:
            return ops[op](num1, num2)
        else:
            return "Unsupported operation. Use +, -, *, or /"
    
    except ValueError:
        # Handle cases where input cannot be converted to float
        return "Invalid numbers. Please enter numeric values."

# Main program execution
expression = input("Enter calculation (e.g., 5 + 5): ")  # Get user input
result = calculate(expression)  # Process the expression
print("Result:", result)  # Display the result
