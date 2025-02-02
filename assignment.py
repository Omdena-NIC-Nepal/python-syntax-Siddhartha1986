def format_string(name, age):
    """
    Create a formatted string using f-strings.
    Args:
        name (str): Person's name
        age (int): Person's age
    Returns:
        str: Formatted string
    """
    return f"My name is {name} and I am {age} years old"

def conditional_check(number):
    """
    Check if a number is greater, lesser, or equal to 10.
    Args:
        number (int): Number to check
    Returns:
        str: "Greater", "Lesser", or "Equal"
    """
    if number > 10:
        return "Greater"
    elif number < 10:
        return "Lesser"
    else:
        return "Equal"

def loop_sum(n):
    """
    Calculate sum of numbers from 1 to n using a loop.
    Args:
        n (int): Upper limit
    Returns:
        int: Sum of numbers
    """
    total = 0
    for i in range( 1, n+1):
        total += i
        
    return total


def list_operations(numbers):
    """
    Perform operations on a list of numbers.
    Args:
        numbers (list): List of numbers
    Returns:
        tuple: (sum, max, min)
    """
    if not numbers:
        return ( 0, None, None)
    
    return ( sum(numbers), max(numbers), min(numbers) )

def dict_operations(students_dict):
    """
    Find students with scores above 80.
    Args:
        students_dict (dict): Dictionary of student names and scores
    Returns:
        list: Names of students with scores > 80
    """
    return [ name for name, score in students_dict.items() if score > 80]
    

def set_operations(list1, list2):
    """
    Find common elements between two lists.
    Args:
        list1 (list): First list
        list2 (list): Second list
    Returns:
        set: Common elements
    """
    return set(list1).intersection(set(list2))

def arithmetic_ops(a, b):
    """
    Perform arithmetic operations.
    Args:
        a (float): First number
        b (float): Second number
    Returns:
        dict: Results of arithmetic operations
    """
    if b == 0:
        division = None
        modulo = None
    else:
        division = a / b
        modulo = a % b

    return {
        "sum": a + b,  # Changed "addition" to "sum"
        "difference": a - b,  # Changed "Subtraction" to "difference"
        "product": a * b,  # Changed "Multiplication" to "product"
        "quotient": division,  # Changed "Division" to "quotient"
        "modulo": modulo  # No change needed
    }


def logical_ops(x, y):
    """
    Perform logical operations.
    Args:
        x (bool): First boolean
        y (bool): Second boolean
    Returns:
        dict: Results of logical operations
    """
    return {
        "and": x and y,  # Changed "AND" to "and"
        "or": x or y,  # Changed "OR" to "or"
        "xor": x ^ y,  # Changed "XOR" to "xor"
        "not_x": not x,  # Changed "NOT x" to "not_x"
        "not_y": not y  # Changed "NOT y" to "not_y"
    }


def bitwise_ops(a, b):
    """
    Perform bitwise operations.
    Args:
        a (int): First integer
        b (int): Second integer
    Returns:
        dict: Results of bitwise operations
    """
    return {
        "and": a & b,  # Changed "Bitwise AND" to "and"
        "or": a | b,  # Changed "Bitwise OR" to "or"
        "xor": a ^ b,  # Changed "Bitwise XOR" to "xor"
        "not_a": ~a,  # Changed "Bitwise NOT a" to "not_a"
        "not_b": ~b,  # Changed "Bitwise NOT b" to "not_b"
        "left_shift_a": a << 1,  # Changed "Left Shift a (<<1)" to "left_shift_a"
        "left_shift_b": b << 1,  # Changed "Left Shift b (<<1)" to "left_shift_b"
        "right_shift_a": a >> 1,  # Changed "Right Shift a (>>1)" to "right_shift_a"
        "right_shift_b": b >> 1  # Changed "Right Shift b (>>1)" to "right_shift_b"
    }
