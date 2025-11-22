# ✅ 1. Leap Year Function
def is_leap(year):
    if not isinstance(year, int):
        raise ValueError("Year must be an integer.")
    return (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)

#Explanation:


#A leap year is divisible by 4.


#But if it’s divisible by 100, it must also be divisible by 400.
#So 2000 → leap year ✅, 1900 → not leap year ❌.



#✅ 2. Conditional Statements Exercise
n = int(input())

if n % 2 != 0:
    print("Weird")
elif n % 2 == 0 and 2 <= n <= 5:
    print("Not Weird")
elif n % 2 == 0 and 6 <= n <= 20:
    print("Weird")
elif n % 2 == 0 and n > 20:
    print("Not Weird")

# Explanation:


# Odd → “Weird”


# Even & 2–5 → “Not Weird”


# Even & 6–20 → “Weird”


# Even & >20 → “Not Weird”



#✅ 3. Even Numbers Between a and b (without loop)
#🔹 Solution 1 — Using if-else:
a = 4
b = 10

evens = [a, a+2, a+4] if a % 2 == 0 else [a+1, a+3, a+5]
print([x for x in evens if x <= b])

#🔹 Solution 2 — Without if-else (Pythonic way):
a = 4
b = 10

print([x for x in range(a + (a % 2), b + 1, 2)])

# Explanation:


# (a % 2) checks if a is odd or even.


# range(start, end, 2) generates only even numbers by skipping every other number.

