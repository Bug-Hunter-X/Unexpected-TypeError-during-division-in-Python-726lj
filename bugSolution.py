def function_with_uncommon_error_solution(a, b):
    try:
        #More robust type handling and validation
        if not isinstance(a,(int,float)) or not isinstance(b,(int,float)):
            raise TypeError("Invalid input types: Both inputs must be numbers.")
        result = a / b
        return result
    except ZeroDivisionError:
        print("Error: Division by zero")
        return None
    except TypeError as e:
        print(f"TypeError: {e}")
        return None

# Example usage
print(function_with_uncommon_error_solution(10, 2))  # Output: 5.0
print(function_with_uncommon_error_solution(10, 0))  # Output: Error: Division by zero
None
print(function_with_uncommon_error_solution("10",2)) # Output:TypeError: Invalid input types: Both inputs must be numbers.
None
print(function_with_uncommon_error_solution(10,"a")) # Output:TypeError: Invalid input types: Both inputs must be numbers.
None
print(function_with_uncommon_error_solution(10.5,2.0)) # Output: 5.25