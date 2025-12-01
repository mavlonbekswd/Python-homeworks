# Create a virtual environment
python -m venv venv

# Activate it
# (on Windows)
venv\Scripts\activate
# (on Mac/Linux)
source venv/bin/activate

# Install some packages for testing
pip install requests numpy pandas
Check installed packages:

bash
Copy code
pip list
✅ 2. Create Custom Modules
📁 Folder structure
css
Copy code
project/
│
├── math_operations.py
├── string_utils.py
└── main.py
math_operations.py
python
Copy code
def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        return "Error: Division by zero"
    return a / b
string_utils.py
python
Copy code
def reverse_string(s):
    return s[::-1]

def count_vowels(s):
    vowels = "aeiouAEIOU"
    return sum(1 for char in s if char in vowels)
main.py (to test your modules)
python
Copy code
import math_operations
import string_utils

print("Add:", math_operations.add(5, 3))
print("Subtract:", math_operations.subtract(10, 4))
print("Multiply:", math_operations.multiply(2, 8))
print("Divide:", math_operations.divide(10, 2))

print("Reverse:", string_utils.reverse_string("Mavlono"))
print("Vowels:", string_utils.count_vowels("Assalomu alaykum"))
✅ 3. Create Custom Packages
📁 Folder structure
markdown
Copy code
project/
│
├── geometry/
│   ├── __init__.py
│   └── circle.py
│
└── file_operations/
    ├── __init__.py
    ├── file_reader.py
    └── file_writer.py
geometry/circle.py
python
Copy code
import math

def calculate_area(radius):
    return math.pi * radius ** 2

def calculate_circumference(radius):
    return 2 * math.pi * radius
file_operations/file_reader.py
python
Copy code
def read_file(file_path):
    try:
        with open(file_path, "r") as f:
            return f.read()
    except FileNotFoundError:
        return "Error: File not found."
file_operations/file_writer.py
python
Copy code
def write_file(file_path, content):
    with open(file_path, "w") as f:
        f.write(content)
    return "File written successfully."
main.py (updated for packages)
python
Copy code
from geometry.circle import calculate_area, calculate_circumference
from file_operations.file_reader import read_file
from file_operations.file_writer import write_file

# Geometry package test
radius = 5
print("Area:", calculate_area(radius))
print("Circumference:", calculate_circumference(radius))

# File operations package test
write_file("example.txt", "Hello, this is Mavlono's test file.")
print(read_file("example.txt"))
