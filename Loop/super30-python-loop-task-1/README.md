# super30-python-loop-task-1
Python for Loop Fundamentals

# Python Basic Programming Challenges

A collection of foundational Python scripts designed to practice loops, conditional statements, lists, dictionaries, and string manipulation.

## 🚀 Challenge Overview

This repository contains solutions to the following 12 Python programming exercises:

### 1. Basic Loops & Arithmetic
* **Numbers 1 to 100:** Prints numbers from 1 to 100 using both `for` loops (with `range()`) and `while` loops.
* **Even Numbers:** Filters and prints all even numbers between 1 and 100 using sequential step-ranges and modulo filtering.
* **Odd Numbers:** Filters and prints all odd numbers between 1 and 100 using sequential step-ranges and modulo filtering.
* **Multiplication Table:** Takes an integer input `n` from the user and prints its multiplication table from 1 up to 20.
* **Sum of Numbers:** Calculates the cumulative sum of numbers from 1 to `n` using a loop.
* **Factorial Calculator:** Accepts a user-input number and calculates its factorial iteratively using a `while` loop without built-in math functions.

### 2. Working with Collections (Lists & Dictionaries)
* **Divisible by 3:** Iterates through the list `numbers = [12, 7, 9, 20, 33, 42, 8, 15]` and appends items divisible by 3 into a new list.
* **String Lengths in a List:** Iterates through `languages = ["Python", "Java", "C++", "JavaScript", "Go"]` and prints each language along with its calculated length.
* **Dictionary Iteration:** Uses the `.items()` method to unpack and print every key-value pair from a `student` profile dictionary.

### 3. String & Algorithm Logic
* **Vowel Counter:** Counts how many total vowels exist in a user-provided string.
* **String Reversal:** Reverses a string (such as `"HELLO"`) using a pure element-wise iteration loop without slicing modifiers or built-in helper tools.
* **Find Maximum:** Scans a list of numbers to extract the largest value manually using logical conditional checks instead of `max()`.

---

## 📂 Repository Structure

The solutions are mapped across the files as follows:

| Challenge Description | Associated Implementation File |
| :--- | :--- |
| Print numbers 1 to 100 | `printnumbers.ipynb` |
| Print all even numbers from 1 to 100 | `evennumbers.ipynb` |
| Print all odd numbers from 1 to 100 | `oddnumbers.ipynb` |
| Multiplication table from 1 to 20 | `multiplication.ipynb` |
| Calculate the sum of numbers from 1 to n | `sumofnumbers.ipynb` |
| Factorial without built-in functions | `factorial.ipynb` |
| Print numbers divisible by 3 | `divisible_3.ipynb` |
| Print languages along with their length | `stringlength.ipynb` |
| Iterate through a student dictionary | `keyvalueprint.ipynb` |
| Count vowels in a string | `vowelscount.ipynb` |
| Reverse a string using a loop | `reversestring.ipynb` |
| Find the largest number from a list | `maxnumber.ipynb` |

---

## 📂 Program File Mapping & Sample Execution

Below is the precise mapping of your submitted notebooks along with their specific inputs, core implementation logic, and expected console outputs.

### 1. Print Numbers 1 to 100
* **File:** `printnumbers.ipynb`
* **Logic Used:** Demonstrates both a standard `for i in range(1, 101)` loop and a conditional `while i <= 100` sequence tracking structure.
* **Sample Output:**
  ```text
  1
  2
  3
  ...
  100
  ```

### 2. Print Even Numbers from 1 to 100
* **File:** `evennumbers.ipynb`
* **Logic Used:** Optimized looping via `range(2, 101, 2)` alongside a fallback condition filter check `if i % 2 == 0` within a manual iteration index.
* **Sample Output:**
  ```text
  2
  4
  6
  ...
  100
  ```

### 3. Print Odd Numbers from 1 to 100
* **File:** `oddnumbers.ipynb`
* **Logic Used:** Implements custom index stepping `range(1, 101, 2)` matching an alternative modulo boundary validator rule `if i % 2 == 1`.
* **Sample Output:**
  ```text
  1
  3
  5
  ...
  99
  ```

### 4. Multiplication Table (1 to 20)
* **File:** `multiplication.ipynb`
* **Logic Used:** Takes a terminal input via `int(input())` and uses `range(1, 21)` to map out products sequentially.
* **Sample Input:** `6`
* **Sample Output:**
  ```text
  Displaying 6 table 
  6 X 1 = 6
  6 X 2 = 12
  ...
  6 X 20 = 120
  ```

### 5. Calculate Factorial Without Built-Ins
* **File:** `factorial.ipynb`
* **Logic Used:** Applies a manual accumulator variable `fact = 1` decremented continuously via a continuous execution `while num_inp >= 1` logic path.
* **Sample Input:** `5`
* **Sample Output:**
  ```text
  Total factorial of 5 is 120
  ```

### 6. Filter Numbers Divisible by 3
* **File:** `divisible_3.ipynb`
* **Logic Used:** Iterates over a designated workspace sequence, scanning for `if i % 3 == 0` flags to build out a refined dynamic list element.
* **Sample Input Array:** `[12, 7, 9, 20, 33, 42, 8, 15]`
* **Sample Output:**
  ```text
  Following numbers are divisible by 3 for given list [12, 7, 9, 20, 33, 42, 8, 15]
  [12, 9, 33, 42, 15]
  ```

### 7. Print String Lengths from a List
* **File:** `stringlength.ipynb`
* **Logic Used:** Steps through elements, tracking character bounds using the native embedded system property layout `len(i)`.
* **Sample Input Array:** `["Python", "Java", "C++", "JavaScript", "Go"]`
* **Sample Output:**
  ```text
  length of Python is 6
  length of Java is 4
  length of C++ is 3
  length of JavaScript is 10
  length of Go is 2
  ```

### 8. Unpack and Iterate a Student Dictionary
* **File:** `keyvalueprint.ipynb`
* **Logic Used:** Safely extracts keys and relational dictionary pairings together dynamically by using the structural loop pattern `for key, value in student.items()`.
* **Sample Input Dictionary:**
  ```python
  student = {"name": "Rahul", "age": 22, "course": "Data Science", "city": "Bangalore"}
  ```
* **Sample Output:**
  ```text
  name : Rahul 
  age : 22 
  course : Data Science 
  city : Bangalore 
  ```

### 9. Reverse a String Manually (No Slicing)
* **File:** `reversestring.ipynb`
* **Logic Used:** Loops forward element-by-element over characters, modifying the destination target variable via head-appending configuration `reversed_str = i + reversed_str`.
* **Sample Input:** `"HELLO"`
* **Sample Output:**
  ```text
  OLLEH
  ```

### 10. Extract Largest Number Without `max()`
* **File:** `maxnumber.ipynb`
* **Logic Used:** Scans linear targets using a simple threshold tracker variable `large_number = 0`. It checks if individual elements exceed the current maximum using `if i > large_number`.
* **Sample Input Array:** `[12, 7, 9, 20, 33, 42, 8, 15, 25, 99, 86]`
* **Sample Output:**
  ```text
  99 is the Largest number from the given list [12, 7, 9, 20, 33, 42, 8, 15, 25, 99, 86] 
  ```

### 11. Sum of Numbers from 1 to n
* **File:** `sumofnumbers.ipynb`
* **Logic Used:** Uses an accumulator variable initialized to 0, then iteratively adds each number from 1 to `n` using a `for` loop with `range(1, n+1)`.
* **Sample Input:** `5`
* **Sample Output:**
  ```text
  Sum of numbers from 1 to 5 is 15
  ```

### 12. Count Vowels in a String
* **File:** `vowelscount.ipynb`
* **Logic Used:** Iterates through each character in the input string and checks if it matches any vowel (a, e, i, o, u) using conditional logic, maintaining a counter variable.
* **Sample Input:** `"Hello World"`
* **Sample Output:**
  ```text
  Total vowels in the string: 3
  ```

---

## 🛠️ Requirements & Setup

### Prerequisites
These scripts require a **Python 3.13+** environment with Jupyter runtime frameworks installed to operate:
```bash
pip install jupyter
```

### Running Locally
```bash
git clone https://github.com/bkvs88/super30-python-loop-task-1
cd super30-python-loop-task-1
jupyter notebook
```

---

## 🛠️ How to Run the Notebooks

### Prerequisites
Ensure you have Jupyter Notebook or JupyterLab installed alongside Python 3.13+:
```bash
pip install jupyter
```

### Execution
Clone the repository and launch the Jupyter interface to interact with your solutions:
```bash
# Clone this repository
git clone https://github.com/bkvs88/super30-python-loop-task-1

# Navigate into the project folder
cd super30-python-loop-task-1

# Start the Jupyter Notebook server
jupyter notebook
```

---

## 📝 Technologies Used
* **Language:** Python 3.13
* **Environment:** Jupyter Notebooks (`.ipynb`)
* **Core Concepts:** `for` loops, `while` loops, conditional branching (`if-else`), sequence structures, dictionary expansion, and manual accumulator algorithms.
