#✅ 1. Modify String with Underscores
def insert_underscores(txt):
    result = ""
    count = 0
    vowels = "aeiouAEIOU"
    for i, ch in enumerate(txt):
        result += ch
        count += 1
        if count == 3:
            # Check if current character is vowel or already followed by "_"
            if ch in vowels or (i + 1 < len(txt) and txt[i + 1] == "_"):
                continue
            if i != len(txt) - 1:
                result += "_"
            count = 0
    return result

# Examples
print(insert_underscores("hello"))       # hel_lo
print(insert_underscores("assalom"))     # ass_alom
print(insert_underscores("abcabcabcdeabcdefabcdefg"))  # abc_abcab_cdeabcd_efabcdef_g

#✅ 2. Integer Squares Exercise
n = int(input())
for i in range(n):
    print(i ** 2)

#✅ 3. Loop-Based Exercises
#Exercise 1: Print first 10 natural numbers
i = 1
while i <= 10:
    print(i)
    i += 1

#Exercise 2: Print number pattern
for i in range(1, 6):
    for j in range(1, i + 1):
        print(j, end=" ")
    print()

#Exercise 3: Sum of all numbers
n = int(input("Enter number: "))
total = 0
for i in range(1, n + 1):
    total += i
print("Sum is:", total)

#Exercise 4: Multiplication table
n = int(input("Enter number: "))
for i in range(1, 11):
    print(n * i)

#Exercise 5: Display numbers from list
numbers = [12, 75, 150, 180, 145, 525, 50]
for num in numbers:
    if num > 500:
        break
    if num > 150:
        continue
    if num % 5 == 0:
        print(num)

#Exercise 6: Count digits
num = int(input("Enter number: "))
count = 0
while num != 0:
    num //= 10
    count += 1
print("Total digits:", count)

#Exercise 7: Reverse number pattern
for i in range(5, 0, -1):
    for j in range(i, 0, -1):
        print(j, end=" ")
    print()

#Exercise 8: Reverse list
list1 = [10, 20, 30, 40, 50]
for i in reversed(list1):
    print(i)

#Exercise 9: Display numbers -10 to -1
for i in range(-10, 0):
    print(i)

#Exercise 10: Display message “Done”
for i in range(5):
    print(i)
else:
    print("Done!")

#Exercise 11: Print all prime numbers
start = 25
end = 50
print("Prime numbers between", start, "and", end, ":")
for num in range(start, end + 1):
    if num > 1:
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                break
        else:
            print(num)

#Exercise 12: Fibonacci series up to 10 terms
n = 10
a, b = 0, 1
print("Fibonacci sequence:")
for _ in range(n):
    print(a, end="  ")
    a, b = b, a + b

#Exercise 13: Factorial of a number
num = int(input("Enter number: "))
factorial = 1
for i in range(1, num + 1):
    factorial *= i
print(f"{num}! = {factorial}")

#✅ 4. Return Uncommon Elements of Lists
def uncommon_elements(list1, list2):
    return [x for x in list1 + list2 if (x not in list1 or x not in list2) or (list1.count(x) != list2.count(x))]

# Examples
print(uncommon_elements([1, 1, 2], [2, 3, 4]))       # [1, 1, 3, 4]
print(uncommon_elements([1, 2, 3], [4, 5, 6]))       # [1, 2, 3, 4, 5, 6]
print(uncommon_elements([1, 1, 2, 3, 4, 2], [1, 3, 4, 5]))  # [2, 2, 5]
