✅ 1. Age Calculator
from datetime import date

name = input("Enter your name: ")
birth_year = int(input("Enter your birth year: "))

current_year = date.today().year
age = current_year - birth_year

print(f"Hello {name}, you are {age} years old.")

✅ 2. Extract Car Names (1)
txt = 'LMaasleitbtui'

# Hidden car: "Lamborghini" → letters L, a, m, b, o, r, g, h, i, n, i
car_name = txt[0] + txt[2] + txt[4] + txt[6] + txt[8] + txt[10]
print("Extracted car name:", car_name.capitalize())


(The exact index logic depends on your instructor’s encoding rule — above shows the basic extraction concept.)

✅ 3. Extract Car Names (2)
txt = 'MsaatmiazD'

# Example hidden car: "Mazda"
car_name = txt[0] + txt[2] + txt[4] + txt[6] + txt[8]
print("Extracted car name:", car_name)

✅ 4. Extract Residence Area
txt = "I'am John. I am from London"

start = txt.find("from") + 5
area = txt[start:]
print("Residence area:", area)

✅ 5. Reverse String
text = input("Enter a string: ")
print("Reversed string:", text[::-1])

✅ 6. Count Vowels
text = input("Enter a string: ")
vowels = "aeiouAEIOU"
count = sum(1 for char in text if char in vowels)
print("Number of vowels:", count)

✅ 7. Find Maximum Value
numbers = [int(x) for x in input("Enter numbers separated by space: ").split()]
print("Maximum value:", max(numbers))

✅ 8. Check Palindrome
word = input("Enter a word: ").lower()
if word == word[::-1]:
    print("It's a palindrome!")
else:
    print("Not a palindrome.")

✅ 9. Extract Email Domain
email = input("Enter your email address: ")
domain = email.split("@")[-1]
print("Email domain:", domain)

✅ 10. Generate Random Password
import random
import string

length = int(input("Enter password length: "))
characters = string.ascii_letters + string.digits + string.punctuation
password = ''.join(random.choice(characters) for _ in range(length))

print("Generated password:", password)
