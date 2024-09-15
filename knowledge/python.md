# Python 3.9 Standard Library User Manual

## Table of Contents

1. [Introduction](#introduction)
2. [Getting Started](#getting-started)
3. [Built-in Functions](#built-in-functions)
4. [Data Types](#data-types)
   - [Numbers](#numbers)
   - [Strings](#strings)
   - [Lists](#lists)
   - [Tuples](#tuples)
   - [Dictionaries](#dictionaries)
   - [Sets](#sets)
5. [Modules and Packages](#modules-and-packages)
6. [Commonly Used Modules](#commonly-used-modules)
   - [os](#os)
   - [sys](#sys)
   - [datetime](#datetime)
   - [math](#math)
   - [random](#random)
   - [json](#json)
   - [re (Regular Expressions)](#re-regular-expressions)
   - [subprocess](#subprocess)
   - [threading](#threading)
   - [logging](#logging)
7. [File Handling](#file-handling)
8. [Exception Handling](#exception-handling)
9. [Conclusion](#conclusion)

---

## Introduction

Python is a versatile and powerful programming language known for its simplicity and readability. One of its greatest strengths is the extensive standard library that comes bundled with Python, offering a wide range of modules and functions for various tasks.

---

## Getting Started

Python 3.9 can be downloaded from the [official website](https://www.python.org/downloads/). After installation, you can run Python scripts using the command line:

```bash
python your_script.py
```

---

## Built-in Functions

Python provides several built-in functions that are always available without importing any module.

**Examples:**

- `print()`: Displays output.
- `len()`: Returns the length of an object.
- `type()`: Returns the type of an object.
- `input()`: Reads a line from input.

---

## Data Types

### Numbers

Python supports integers, floating-point numbers, and complex numbers.

```python
x = 10          # Integer
y = 3.14        # Float
z = 2 + 3j      # Complex number
```

### Strings

Strings are sequences of characters.

```python
s = "Hello, World!"
```

**Common String Methods:**

- `s.upper()`: Converts to uppercase.
- `s.lower()`: Converts to lowercase.
- `s.split(",")`: Splits the string into a list.

### Lists

Ordered, mutable collections of items.

```python
my_list = [1, 2, 3, 'a', 'b', 'c']
```

**List Methods:**

- `my_list.append(4)`: Adds an item.
- `my_list.remove('a')`: Removes an item.

### Tuples

Ordered, immutable collections.

```python
my_tuple = (1, 2, 3)
```

### Dictionaries

Key-value pairs, unordered and mutable.

```python
my_dict = {'name': 'Alice', 'age': 30}
```

**Dictionary Methods:**

- `my_dict.keys()`: Returns all keys.
- `my_dict.values()`: Returns all values.

### Sets

Unordered collections of unique elements.

```python
my_set = {1, 2, 3, 3}
# my_set will be {1, 2, 3}
```

---

## Modules and Packages

Modules are files containing Python definitions and statements. Packages are a way of structuring modules hierarchically.

**Importing Modules:**

```python
import math
from datetime import datetime
```

---

## Commonly Used Modules

### os

Provides functions for interacting with the operating system.

**Examples:**

```python
import os

current_directory = os.getcwd()
os.mkdir('new_folder')
```

### sys

Access system-specific parameters and functions.

**Examples:**

```python
import sys

sys.exit()
print(sys.version)
```

### datetime

Work with dates and times.

**Examples:**

```python
from datetime import datetime

now = datetime.now()
print(now.strftime("%Y-%m-%d %H:%M:%S"))
```

### math

Mathematical functions.

**Examples:**

```python
import math

result = math.sqrt(16)
print(math.pi)
```

### random

Generate random numbers.

**Examples:**

```python
import random

number = random.randint(1, 100)
choice = random.choice(['apple', 'banana', 'cherry'])
```

### json

Encode and decode JSON data.

**Examples:**

```python
import json

data = {'name': 'Bob', 'age': 25}
json_str = json.dumps(data)
data_back = json.loads(json_str)
```

### re (Regular Expressions)

String searching and manipulation using patterns.

**Examples:**

```python
import re

pattern = r'\d+'
result = re.findall(pattern, 'There are 2 apples and 5 bananas')
```

### subprocess

Spawn new processes, connect to their input/output/error pipes.

**Examples:**

```python
import subprocess

subprocess.run(['ls', '-l'])
```

### threading

Run multiple threads concurrently.

**Examples:**

```python
import threading

def worker():
    print("Worker thread")

thread = threading.Thread(target=worker)
thread.start()
```

### logging

Flexible logging system.

**Examples:**

```python
import logging

logging.basicConfig(level=logging.INFO)
logging.info('This is an info message')
```

---

## File Handling

Open, read, write, and close files.

**Examples:**

```python
# Writing to a file
with open('example.txt', 'w') as file:
    file.write('Hello, World!')

# Reading from a file
with open('example.txt', 'r') as file:
    content = file.read()
```

---

## Exception Handling

Manage errors using try-except blocks.

**Examples:**

```python
try:
    result = 10 / 0
except ZeroDivisionError:
    print("Cannot divide by zero")
finally:
    print("This will always execute")
```

---

## Conclusion

Python's standard library provides a rich set of modules and functions that greatly enhance the language's capabilities. From file handling to network communication, the standard library has tools for almost any task, making Python a powerful choice for a wide range of applications.

---

**References:**

- Official Documentation: [https://docs.python.org/3.9/library/](https://docs.python.org/3.9/library/)