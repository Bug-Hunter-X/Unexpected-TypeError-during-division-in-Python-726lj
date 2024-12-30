def function_with_uncommon_error(a, b):
    try:
        result = a / b
        return result
    except ZeroDivisionError:
        print("Error: Division by zero")
        return None
    except TypeError:
        if isinstance(a,(int,float)) and isinstance(b,(int,float)):
            print("Uncommon Error: unexpected TypeError")
            return None
        else:
            print("Invalid input types")
            return None

# Example usage
print(function_with_uncommon_error(10, 2))  # Output: 5.0
print(function_with_uncommon_error(10, 0))  # Output: Error: Division by zero
None
print(function_with_uncommon_error("10",2)) # Output:Invalid input types
None
print(function_with_uncommon_error(10,"a")) # Output:Invalid input types
None
print(function_with_uncommon_error(10.5,2.0)) # Output: 5.25