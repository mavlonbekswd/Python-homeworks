Exception Handling Exercises
1. Handle ZeroDivisionError
try:
    a = int(input("Enter a number: "))
    b = int(input("Enter another number: "))
    result = a / b
    print("Result:", result)
except ZeroDivisionError:
    print("Error: Cannot divide by zero.")

2. Handle ValueError for Invalid Integer Input
try:
    num = int(input("Enter an integer: "))
    print("You entered:", num)
except ValueError:
    print("Error: That is not a valid integer.")

3. Handle FileNotFoundError
try:
    with open("sample.txt", "r") as f:
        print(f.read())
except FileNotFoundError:
    print("Error: File not found.")

4. Handle TypeError for Non-Numeric Inputs
try:
    x = input("Enter first number: ")
    y = input("Enter second number: ")
    result = float(x) + float(y)
    print("Sum:", result)
except ValueError:
    raise TypeError("Inputs must be numeric.")

5. Handle PermissionError
try:
    with open("/protected/file.txt", "r") as f:
        print(f.read())
except PermissionError:
    print("Error: You don't have permission to access this file.")

6. Handle IndexError
numbers = [10, 20, 30]
try:
    print(numbers[5])
except IndexError:
    print("Error: Index out of range.")

7. Handle KeyboardInterrupt
try:
    num = input("Enter a number: ")
    print("You entered:", num)
except KeyboardInterrupt:
    print("\nInput cancelled by user.")

8. Handle ArithmeticError
try:
    x = 10 / 0
except ArithmeticError as e:
    print("Arithmetic Error:", e)

9. Handle UnicodeDecodeError
try:
    with open("textfile.txt", "r", encoding="ascii") as f:
        print(f.read())
except UnicodeDecodeError:
    print("Error: Unable to decode file due to encoding issue.")

10. Handle AttributeError
try:
    num = 10
    num.append(5)
except AttributeError:
    print("Error: Attribute does not exist for this object.")

File Input/Output Exercises
1. Read Entire File
with open("data.txt", "r") as f:
    print(f.read())

2. Read First n Lines
n = int(input("Enter number of lines: "))
with open("data.txt", "r") as f:
    for i in range(n):
        print(f.readline(), end="")

3. Append Text and Display
with open("data.txt", "a") as f:
    f.write("\nAppended line.")
with open("data.txt", "r") as f:
    print(f.read())

4. Read Last n Lines
n = int(input("Enter number of last lines: "))
with open("data.txt", "r") as f:
    lines = f.readlines()
    print("".join(lines[-n:]))

5. Read File Line by Line into List
with open("data.txt", "r") as f:
    lines = f.readlines()
print(lines)

6. Read File Line by Line into Variable
with open("data.txt", "r") as f:
    text = f.read()
print(text)

7. Read File into Array
with open("data.txt", "r") as f:
    array = [line.strip() for line in f]
print(array)

8. Find Longest Words
with open("data.txt", "r") as f:
    words = f.read().split()
    longest = max(words, key=len)
print("Longest word:", longest)

9. Count Number of Lines
with open("data.txt", "r") as f:
    print("Number of lines:", len(f.readlines()))

10. Count Word Frequency
from collections import Counter
with open("data.txt", "r") as f:
    words = f.read().split()
print(Counter(words))

11. Get File Size
import os
print("File size:", os.path.getsize("data.txt"), "bytes")

12. Write List to File
lines = ["Hello", "Python", "World"]
with open("output.txt", "w") as f:
    f.writelines(line + "\n" for line in lines)

13. Copy File Contents
with open("data.txt", "r") as src, open("copy.txt", "w") as dest:
    dest.write(src.read())

14. Combine Lines from Two Files
with open("file1.txt") as f1, open("file2.txt") as f2:
    for a, b in zip(f1, f2):
        print(a.strip() + " " + b.strip())

15. Read Random Line
import random
with open("data.txt", "r") as f:
    lines = f.readlines()
print(random.choice(lines))

16. Check if File is Closed
f = open("data.txt", "r")
print(f.closed)  # False
f.close()
print(f.closed)  # True

17. Remove Newline Characters
with open("data.txt", "r") as f:
    lines = [line.strip() for line in f]
print(lines)

18. Count Words in a File
with open("data.txt", "r") as f:
    text = f.read().replace(",", " ")
    print("Word count:", len(text.split()))

19. Extract Characters into a List
chars = []
for filename in ["file1.txt", "file2.txt", "file3.txt"]:
    with open(filename, "r") as f:
        chars.extend(list(f.read()))
print(chars)

20. Generate 26 Text Files (A.txt → Z.txt)
import string
for letter in string.ascii_uppercase:
    open(f"{letter}.txt", "w").close()

21. Create Alphabet File with Specified Letters per Line
import string

letters_per_line = 5
letters = string.ascii_uppercase

with open("alphabet.txt", "w") as f:
    for i in range(0, len(letters), letters_per_line):
        f.write(" ".join(letters[i:i + letters_per_line]) + "\n")
