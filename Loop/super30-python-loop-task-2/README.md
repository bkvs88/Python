# super30-python-loop-task-2
Intermediate Loops &amp; Loop Control
# super30-python-loop-task-2

## Intermediate Loops & Loop Control

This repository contains Python Jupyter notebooks demonstrating advanced loop concepts and loop control statements. Each notebook addresses specific programming challenges related to loops, including loop control (continue, break), conditional logic, and pattern generation.

---

## 📚 Notebooks and Questions Map

| # | Question | Notebook | Description |
|---|----------|----------|-------------|
| 1 | Print numbers from 1–100 but skip numbers divisible by 5 using `continue` | [`divisible_by_5.ipynb`](./divisible_by_5.ipynb) | Demonstrates the use of the `continue` statement to skip iterations based on a condition |
| 2 | Iterate from 1–100 and stop when you encounter the first number divisible by both 7 and 11 | [`divided_by_7_11.ipynb`](./divided_by_7_11.ipynb) | Shows how to use a loop with a break statement to exit early when a condition is met |
| 3 | Search for a user-provided number inside a list using `for-else` to print "Number Found" or "Number Not Found" | [`forelse.ipynb`](./forelse.ipynb) | Illustrates the use of Python's `for-else` construct for conditional logic after loop completion |
| 4 | Given `names = ["Aman", "Ravi", "Sudhanshu", "Priya", "Anjali"]`, use `enumerate()` to display numbered list | [`use_enumerate.ipynb`](./use_enumerate.ipynb) | Demonstrates `enumerate()` function to get both index and value while iterating |
| 5 | Print the following pattern: *, **, ***, ****, ***** | [`pattern_print_forward.ipynb`](./pattern_print_forward.ipynb) | Creates a forward pattern using nested loops |
| 6 | Print the following pattern: *****, ****, ***, **, * | [`pattern_print_backward.ipynb`](./pattern_print_backward.ipynb) | Creates a backward/reverse pattern using nested loops |
| 7 | Generate multiplication tables from 1 to 10 using nested loops | [`gen_multiply_tables.ipynb`](./gen_multiply_tables.ipynb) | Nested loops to generate and display multiplication tables |
| 8 | Find all numbers between 1 and 200 divisible by both 3 and 5 | [`divisible_by3_5.ipynb`](./divisible_by3_5.ipynb) | Uses loops with conditional statements to find numbers meeting multiple criteria |
| 9 | Given a list containing duplicate elements, create another list containing only unique elements without using `set()` | [`suppress_duplicates.ipynb`](./suppress_duplicates.ipynb) | Demonstrates list manipulation and iteration to remove duplicates manually |
| 10 | Given `numbers = [10, -4, 8, -2, 0, 15, -9, 21]`, count positive numbers, negative numbers, and zeros | [`count_postv_negtv_zero.ipynb`](./count_postv_negtv_zero.ipynb) | Uses loops with conditional logic to categorize and count numbers |
| 11 | Write a program to determine whether a number is prime using a loop | [`prime_number_check.ipynb`](./prime_number_check.ipynb) | Implements prime number checking logic using loops and conditional statements |
| 12 | Print all prime numbers between 1 and 100 | [`prime_numbers_below100.ipynb`](./prime_numbers_below100.ipynb) | Combines prime checking with loops to generate all primes in a range |

---

## 🎯 Key Concepts Covered

- **Loop Control Statements**: `break` and `continue`
- **Loop Alternatives**: `for-else` construct
- **Nested Loops**: Creating patterns and multiplication tables
- **Iteration Utilities**: `enumerate()` function
- **Conditional Logic**: Filtering and categorizing data within loops
- **Prime Numbers**: Algorithm implementation using loops
- **List Manipulation**: Working with lists and removing duplicates

### 1. **Loop Control Statements**

#### `break` Statement
The `break` statement is used to exit or terminate a loop prematurely when a certain condition is met. Once `break` is executed, the loop is immediately terminated and the program continues with the statement following the loop.

**Use Case**: Stopping iteration when a target value is found
```python
for num in range(1, 101):
    if num % 7 == 0 and num % 11 == 0:
        print(f"Found: {num}")
        break  # Exit loop immediately
```

**Benefits:**
- Improves performance by avoiding unnecessary iterations
- Simplifies code when you need to find the first occurrence of something
- Prevents redundant computations after a condition is satisfied

**Notebook Reference**: [`divided_by_7_11.ipynb`](./divided_by_7_11.ipynb)

---

#### `continue` Statement
The `continue` statement skips the rest of the current iteration and jumps to the next iteration of the loop. Unlike `break`, the loop continues running.

**Use Case**: Skipping certain values without terminating the loop
```python
for num in range(1, 101):
    if num % 5 == 0:
        continue  # Skip this iteration
    print(num)  # Only prints numbers not divisible by 5
```

**Benefits:**
- Allows conditional processing of loop iterations
- Keeps code clean and readable by avoiding nested if-else blocks
- Useful for filtering or excluding specific items from processing

**Notebook Reference**: [`divisible_by_5.ipynb`](./divisible_by_5.ipynb)

---

### 2. **Loop Alternatives: for-else Construct**

Python's `for-else` construct is a unique feature that executes the `else` block only if the loop completes normally (without encountering a `break` statement).

**Syntax:**
```python
for item in iterable:
    if condition:
        break
else:
    # Executed only if break was NOT called
    print("Loop completed without break")
```

**Practical Example:**
```python
numbers = [2, 4, 6, 8, 10]
search_num = 5

for num in numbers:
    if num == search_num:
        print("Number Found")
        break
else:
    print("Number Not Found")
```

**When to Use:**
- Searching for an element in a list
- Validating that all items meet certain criteria
- Replacing traditional flag variables used to track loop completion

**Advantages:**
- More Pythonic and readable than using flag variables
- Eliminates the need for extra boolean checks after loops
- Makes the intent of the code clearer

**Notebook Reference**: [`forelse.ipynb`](./forelse.ipynb)

---

### 3. **Nested Loops**

Nested loops are loops within loops. The inner loop executes completely for each iteration of the outer loop, creating a powerful mechanism for working with multi-dimensional data or generating patterns.

**Common Applications:**

#### Pattern Generation
```python
# Forward pattern
for i in range(1, 6):
    for j in range(i):
        print("*", end="")
    print()
# Output:
# *
# **
# ***
# ****
# *****
```

#### Multiplication Tables
```python
for i in range(1, 11):
    for j in range(1, 11):
        print(f"{i} × {j} = {i*j}", end="\t")
    print()
```

**Key Characteristics:**
- Time Complexity: O(n²) or higher depending on nesting depth
- Each inner loop iteration depends on the outer loop
- Useful for 2D data structures (matrices, grids)
- Can become computationally expensive with many iterations

**Notebook References**: 
- [`pattern_print_forward.ipynb`](./pattern_print_forward.ipynb)
- [`pattern_print_backward.ipynb`](./pattern_print_backward.ipynb)
- [`gen_multiply_tables.ipynb`](./gen_multiply_tables.ipynb)

---

### 4. **Iteration Utilities: enumerate() Function**

The `enumerate()` function returns an iterator that produces pairs of (index, value) for each item in an iterable. It's essential for cases where you need both the position and value.

**Syntax:**
```python
for index, value in enumerate(iterable, start=0):
    # start parameter is optional (default is 0)
```

**Practical Example:**
```python
names = ["Aman", "Ravi", "Sudhanshu", "Priya", "Anjali"]
for index, name in enumerate(names, start=1):
    print(f"{index} {name}")
# Output:
# 1 Aman
# 2 Ravi
# 3 Sudhanshu
# 4 Priya
# 5 Anjali
```

**Advantages:**
- Cleaner than using range(len(iterable))
- More readable and Pythonic
- Avoids manual counter variables
- Can customize the starting index with the `start` parameter

**Common Use Cases:**
- Creating numbered lists
- Accessing both index and value simultaneously
- Avoiding off-by-one errors in manual indexing

**Notebook Reference**: [`use_enumerate.ipynb`](./use_enumerate.ipynb)

---

### 5. **Conditional Logic in Loops**

Combining conditional statements within loops allows for powerful filtering, categorization, and data processing capabilities.

**Multiple Conditions:**
```python
# Finding numbers divisible by BOTH 3 and 5
for num in range(1, 201):
    if num % 3 == 0 and num % 5 == 0:
        print(num)
```

**Categorization:**
```python
numbers = [10, -4, 8, -2, 0, 15, -9, 21]
positive = negative = zeros = 0

for num in numbers:
    if num > 0:
        positive += 1
    elif num < 0:
        negative += 1
    else:
        zeros += 1
```

**Use Cases:**
- Filtering data based on specific criteria
- Counting items by categories
- Validating data during iteration
- Implementing complex search logic

**Notebook References**:
- [`divisible_by3_5.ipynb`](./divisible_by3_5.ipynb)
- [`count_postv_negtv_zero.ipynb`](./count_postv_negtv_zero.ipynb)

---

### 6. **Prime Number Detection**

A prime number is a natural number greater than 1 that has no positive divisors other than 1 and itself. Implementing prime checking with loops is a fundamental algorithm.

**Algorithm:**
```python
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True
```

**Key Optimizations:**
- Only check divisors up to √n (reduces iterations by ~50%)
- Start checking from 2 (smallest prime)
- Return False immediately when a divisor is found
- Skip even numbers (except 2) in practice for speed

**Applications:**
- Cryptography and security
- Number theory problems
- Data validation
- Algorithm efficiency testing

**Notebook References**:
- [`prime_number_check.ipynb`](./prime_number_check.ipynb)
- [`prime_numbers_below100.ipynb`](./prime_numbers_below100.ipynb)

---

### 7. **List Manipulation: Removing Duplicates Without set()**

Manually removing duplicates demonstrates loop iteration and list methods while avoiding built-in convenience functions.

**Approach:**
```python
duplicates = [1, 2, 2, 3, 3, 3, 4, 5, 5]
unique = []

for item in duplicates:
    if item not in unique:
        unique.append(item)

print(unique)  # [1, 2, 3, 4, 5]
```

**How It Works:**
1. Iterate through each item in the original list
2. Check if the item already exists in the unique list
3. If not found, add it to the unique list
4. Skip duplicates found

**Performance Considerations:**
- Time Complexity: O(n²) because `in` operation is O(n) for lists
- For large lists, `set()` approach is significantly faster
- This method preserves original order (unlike set conversion)

**Educational Value:**
- Teaches the fundamental logic behind deduplication
- Demonstrates list membership checking
- Shows the limitations of naive approaches
- Motivates the use of more efficient data structures

**Notebook Reference**: [`suppress_duplicates.ipynb`](./suppress_duplicates.ipynb)

---

## 📖 How to Use

1. Clone the repository:
   ```bash
   git clone https://github.com/bkvs88/super30-python-loop-task-2.git
   ```

2. Navigate to the repository:
   ```bash
   cd super30-python-loop-task-2
   ```

3. Open Jupyter Notebook:
   ```bash
   jupyter notebook
   ```

4. Select any `.ipynb` file to view and run the code examples


---

## 💡 Learning Outcomes

By working through these notebooks, you will understand:

- **Fundamental Control Flow**: How to manage loop execution with `break` and `continue`
- **Advanced Loop Patterns**: Using `for-else` for elegant search and validation logic
- **Nested Loops**: Creating complex patterns and processing multi-dimensional data
- **Iteration Techniques**: Using `enumerate()` and other iteration utilities effectively
- **Algorithmic Thinking**: Implementing algorithms like prime detection and deduplication
- **Data Processing**: Filtering, categorizing, and manipulating data within loops
- **Code Optimization**: Writing efficient and readable loop-based solutions
- **Problem Solving**: Applying loops to solve real-world programming challenges
