# Super30 - Python Functions (Task 1)

## 1. Introduction to Python Functions

### What is a Python Function?

A Python function is a reusable block of code that performs a specific task. Functions allow you to:
- **Break down complex problems** into smaller, manageable pieces
- **Avoid code repetition** by writing once and calling multiple times
- **Organize code logically** for better readability and maintenance
- **Test code more easily** by isolating functionality

### Basic Syntax Structure

```python
def function_name(parameters):
    """Optional docstring explaining what the function does."""
    # Function body - the code that executes
    return value  # Optional - returns a value to the caller
```

**Example:**
```python
def greet(name):
    """Greet a person by name."""
    return f"Hello, {name}!"

# Calling the function
message = greet("Alice")
print(message)  # Output: Hello, Alice!
```

### Key Concepts to Know

1. **Function Definition**: Created using the `def` keyword
2. **Parameters**: Named placeholders in the function definition
3. **Arguments**: Actual values passed when calling the function
4. **Return Statement**: Sends a value back to the caller
5. **Scope**: Variables defined inside a function are local to that function
6. **Default Parameters**: Provide default values if no argument is passed

### Parameters vs Arguments

| Concept | Definition | Example |
|---------|-----------|---------|
| **Parameters** | Variables listed in function definition | `def add(a, b):` — `a` and `b` are parameters |
| **Arguments** | Actual values passed when calling the function | `add(5, 3)` — `5` and `3` are arguments |
| **Positional Arguments** | Arguments matched by position | `add(5, 3)` matches `a=5, b=3` |
| **Keyword Arguments** | Arguments passed with explicit parameter names | `add(a=5, b=3)` or `add(b=3, a=5)` |
| **Default Parameters** | Parameters with predefined values | `def discount(price, percent=10):` |

**Example showing positional and keyword arguments:**
```python
def concat(a, b, sep=' '):
    """Concatenate two strings with a separator."""
    return f"{a}{sep}{b}"

# Positional call
print(concat('hello', 'world'))  # 'hello world'

# Keyword call
print(concat(a='hello', b='world', sep='-'))  # 'hello-world'

# Mixed call
print(concat('hello', 'world', sep='_'))  # 'hello_world'
```

### Returning Data

- `print()` writes output to the console and returns `None`
- `return` sends a value back to the caller so it can be used, assigned to variables, or passed to other functions
- Functions can return a single value, multiple values (as a tuple), or nothing (`None`)

**Comparison: print() vs return**

```python
def greet_print(name):
    """Greet using print (output only, no return value)."""
    print(f"Hello, {name}!")

def greet_return(name):
    """Greet using return (value can be reused by caller)."""
    return f"Hello, {name}!"

# Using print(): the function prints but we cannot reuse the value
res = greet_print("Alice")
print("res from greet_print:", res)  # prints: res from greet_print: None

# Using return(): the caller receives the value and can reuse it
msg = greet_return("Bob")
print("Message:", msg)  # prints: Message: Hello, Bob!
upper_msg = msg.upper()  # We can transform the returned value
print(upper_msg)  # BOB!
```

### Quick Summary

| Aspect | Details |
|--------|---------|
| **Why Functions?** | Reusability, organization, testability |
| **Definition** | Use `def keyword(parameters):` |
| **Calling** | `function_name(arguments)` |
| **Parameters** | Placeholders in definition; can have defaults |
| **Arguments** | Actual values passed; can be positional or keyword |
| **Return** | Sends value back; enables reuse and chaining |
| **Scope** | Variables inside function are local by default |

---

## 2. Questions & Implementations Map

| # | Question | Notebook File | Function Signature | Key Concept |
|---|----------|----------------|-------------------|------------|
| 1 | Create a function that returns the addition of two numbers. | `add_fun.ipynb` | `def add(a, b)` | Basic arithmetic operation |
| 2 | Create functions for subtraction, multiplication, and division. | `sub_fun.ipynb`, `multiplication_fun.ipynb`, `division_fun.ipynb` | `def subtract(a, b)`, `def multiply(a, b)`, `def divide(a, b)` | Basic arithmetic operations |
| 3 | Create a function that determines whether a number is even or odd. | `number_odd_even_check.ipynb` | `def is_even(n)` | Conditional logic, modulo operator |
| 4 | Create a function that returns the largest of three numbers without using max(). | `fun_max_number.ipynb` | `def largest_of_three(a, b, c)` | Conditional comparisons |
| 5 | Create a function that calculates factorial. | `fact_fun.ipynb` | `def factorial(n)` | Iterative loops, input validation |
| 6 | Create a function that checks whether a number is prime. | `prime_check_fun.ipynb` | `def is_prime(n)` | Optimized loop logic |
| 7 | Create `def calculate_discount(price, discount=10)` where the default discount is 10%. | `default_var_fun.ipynb` | `def calculate_discount(price, discount=10)` | Default parameters, percentage calculations |
| 8 | Create a function that accepts a list and returns its sum without using sum(). | `accept_list_sum_fun.ipynb` | `def sum_list(numbers)` | List iteration, accumulation |
| 9 | Create a function that accepts a string and returns the number of vowels. | `vowels_check_fun.ipynb` | `def count_vowels(s)` | String iteration, set membership |
| 10 | Create a function that accepts a string and determines whether it is a palindrome. | `palindrome_check_fun.ipynb` | `def is_palindrome(s)` | String manipulation, comparison |
| 11 | Create a function that accepts name, age, course and returns a formatted student profile. Use both positional and keyword arguments while calling it. | `accept_and_display_fun.ipynb` | `def student_profile(name, age, course)` | Positional and keyword arguments |

---

## 3. Task: Implementations

Below are implementations for all requested functions with example usage.

```python
# 1) add(a, b)
def add(a, b):
    """
    Return the sum of two numbers.
    
    Args:
        a (int/float): First number
        b (int/float): Second number
    
    Returns:
        int/float: The sum of a and b
    
    Example:
        >>> add(2, 3)
        5
    """
    return a + b

# 2) basic arithmetic functions

def subtract(a, b):
    """
    Return the difference of two numbers.
    
    Args:
        a (int/float): First number (minuend)
        b (int/float): Second number (subtrahend)
    
    Returns:
        int/float: The difference (a - b)
    
    Example:
        >>> subtract(5, 2)
        3
    """
    return a - b

def multiply(a, b):
    """
    Return the product of two numbers.
    
    Args:
        a (int/float): First number
        b (int/float): Second number
    
    Returns:
        int/float: The product of a and b
    
    Example:
        >>> multiply(3, 4)
        12
    """
    return a * b

def divide(a, b):
    """
    Return the quotient of two numbers.
    
    Args:
        a (int/float): Dividend (numerator)
        b (int/float): Divisor (denominator)
    
    Returns:
        float: The quotient (a / b)
    
    Raises:
        ValueError: If b (divisor) is zero
    
    Example:
        >>> divide(10, 2)
        5.0
    """
    if b == 0:
        raise ValueError("Division by zero is not allowed")
    return a / b

# 3) check even or odd

def is_even(n):
    """
    Check whether a number is even.
    
    A number is even if it is divisible by 2 (remainder is 0).
    
    Args:
        n (int): The number to check
    
    Returns:
        bool: True if n is even, False otherwise
    
    Example:
        >>> is_even(4)
        True
        >>> is_even(5)
        False
    """
    return n % 2 == 0

# 4) largest of three numbers (without using max())

def largest_of_three(a, b, c):
    """
    Return the largest of three numbers without using the max() function.
    
    Uses conditional comparisons to determine the maximum value.
    
    Args:
        a (int/float): First number
        b (int/float): Second number
        c (int/float): Third number
    
    Returns:
        int/float: The largest of the three numbers
    
    Example:
        >>> largest_of_three(5, 9, 2)
        9
    """
    largest = a
    if b > largest:
        largest = b
    if c > largest:
        largest = c
    return largest

# 5) factorial (iterative)

def factorial(n):
    """
    Calculate the factorial of a number.
    
    The factorial of n (denoted n!) is the product of all positive integers
    from 1 to n. For example: 5! = 1 × 2 × 3 × 4 × 5 = 120.
    By definition, 0! = 1.
    
    Args:
        n (int): A non-negative integer
    
    Returns:
        int: The factorial of n
    
    Raises:
        ValueError: If n is negative (factorial undefined for negative numbers)
    
    Example:
        >>> factorial(5)
        120
        >>> factorial(0)
        1
    """
    if n < 0:
        raise ValueError("Factorial is not defined for negative numbers")
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result

# 6) check prime

def is_prime(n):
    """
    Check whether a number is prime.
    
    A prime number is a natural number greater than 1 that has no positive divisors
    other than 1 and itself. Uses an optimized algorithm that checks divisibility
    only up to the square root of n.
    
    Args:
        n (int): The number to check
    
    Returns:
        bool: True if n is prime, False otherwise
    
    Example:
        >>> is_prime(13)
        True
        >>> is_prime(10)
        False
    """
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0:
        return False
    i = 3
    while i * i <= n:
        if n % i == 0:
            return False
        i += 2
    return True

# 7) calculate_discount(price, discount=10)

def calculate_discount(price, discount=10):
    """
    Calculate the final price after applying a discount percentage.
    
    Args:
        price (int/float): The original price (must be non-negative)
        discount (int/float): The discount percentage (default 10). 
                             Must be between 0 and 100.
    
    Returns:
        float: The final price after discount applied
    
    Raises:
        ValueError: If price is negative or discount is not between 0 and 100
    
    Example:
        >>> calculate_discount(100)
        90.0
        >>> calculate_discount(100, discount=25)
        75.0
    """
    if price < 0:
        raise ValueError("Price cannot be negative")
    if discount < 0 or discount > 100:
        raise ValueError("Discount must be between 0 and 100")
    return price * (1 - discount / 100)

# 8) sum_list without using sum()

def sum_list(numbers):
    """
    Calculate the sum of all numbers in a list without using the built-in sum() function.
    
    Iterates through the list and accumulates the total using a for loop.
    
    Args:
        numbers (list): A list of numbers (int or float)
    
    Returns:
        int/float: The sum of all numbers in the list
    
    Example:
        >>> sum_list([1, 2, 3, 4])
        10
    """
    total = 0
    for n in numbers:
        total += n
    return total

# 9) count vowels in a string

def count_vowels(s):
    """
    Count the number of vowels in a string.
    
    Vowels are defined as 'a', 'e', 'i', 'o', 'u' (and their uppercase variants).
    Uses a set for efficient membership checking.
    
    Args:
        s (str): The input string
    
    Returns:
        int: The count of vowels in the string
    
    Example:
        >>> count_vowels('Hello World')
        3
    """
    vowels = set('aeiouAEIOU')
    count = 0
    for ch in s:
        if ch in vowels:
            count += 1
    return count

# 10) check palindrome

def is_palindrome(s):
    """
    Check whether a string is a palindrome.
    
    A palindrome reads the same forwards and backwards. This function ignores
    spaces, punctuation, and capitalization. For example, "A man, a plan, a canal: Panama"
    is a palindrome.
    
    Args:
        s (str): The input string
    
    Returns:
        bool: True if s is a palindrome, False otherwise
    
    Example:
        >>> is_palindrome('A man, a plan, a canal: Panama')
        True
        >>> is_palindrome('hello')
        False
    """
    cleaned = ''.join(ch.lower() for ch in s if ch.isalnum())
    return cleaned == cleaned[::-1]

# 11) student profile

def student_profile(name, age, course):
    """
    Return a formatted student profile string.
    
    Accepts student information and returns a formatted multi-line profile
    with name, age, and course on separate lines.
    
    Args:
        name (str): The student's name
        age (int): The student's age
        course (str): The course the student is enrolled in
    
    Returns:
        str: A formatted profile string with lines separated by newlines
    
    Example:
        >>> print(student_profile('Alice', 22, 'Physics'))
        Name: Alice
        Age: 22
        Course: Physics
    """
    return f"Name: {name}\nAge: {age}\nCourse: {course}"

# Usage examples (positional and keyword arguments):
if __name__ == '__main__':
    print('add(2,3)=', add(2,3))
    print('subtract(5,2)=', subtract(5,2))
    print('multiply(3,4)=', multiply(3,4))
    print('divide(10,2)=', divide(10,2))

    print('is_even(4)=', is_even(4))
    print('largest_of_three(5,9,2)=', largest_of_three(5,9,2))
    print('factorial(5)=', factorial(5))
    print('is_prime(13)=', is_prime(13))

    print('calculate_discount(100)=', calculate_discount(100))
    print('calculate_discount(100, discount=25)=', calculate_discount(100, discount=25))

    print('sum_list([1,2,3,4])=', sum_list([1,2,3,4]))
    print("count_vowels('Hello World')=", count_vowels('Hello World'))
    print("is_palindrome('A man, a plan, a canal: Panama')=", is_palindrome('A man, a plan, a canal: Panama'))

    # student_profile called with positional args
    print('\nStudent profile (positional):')
    print(student_profile('Alice', 22, 'Physics'))

    # student_profile called with keyword args
    print('\nStudent profile (keyword):')
    print(student_profile(name='Bob', course='Mathematics', age=24))
```

## Notes & Best Practices

- Functions use `return` when their result is needed for further computation or testing. Use `print()` only for direct console output/demo.
- Input validation (where appropriate) raises exceptions for clarity (e.g., division by zero, negative factorial input).
- Always use descriptive function names and include docstrings.
- Keep functions focused on a single task for better reusability and testing.

---

## Repository Structure

Each exercise has a dedicated Jupyter Notebook file for interactive learning and experimentation. Refer to Section 2's "Questions & Implementations Map" table for the correct notebook file names.

If you want, I can also create individual `functions.py` files for each notebook or a combined `functions.py` file with all implementations. Let me know!
