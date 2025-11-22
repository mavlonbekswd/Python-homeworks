
# 1. Sort a Dictionary by Value
my_dict = {1: 20, 2: 10, 3: 30}
ascending = dict(sorted(my_dict.items(), key=lambda x: x[1]))
descending = dict(sorted(my_dict.items(), key=lambda x: x[1], reverse=True))
print("Ascending:", ascending)
print("Descending:", descending)

#2. Add a Key to a Dictionary
#Write a Python script to add a key to a dictionary.

numbers = { 0 : 10,
            1 : 20,
           }
numbers [2] = 30
numbers

# 3. Concatenate Multiple Dictionaries
dic1 = {1: 10, 2: 20}
dic2 = {3: 30, 4: 40}
dic3 = {5: 50, 6: 60}
merged = {**dic1, **dic2, **dic3}
print("Merged:", merged)

#4. Generate a Dictionary with Squares
n = int(input("Enter a number: "))

squares = {}  # bo‘sh dictionary

for i in range(1, n + 1):
    squares[i] = i ** 2  # key: value qo‘shyapmiz

print(squares)

#5. Dictionary of Squares (1 to 15)

square_dict = {}

for number in range(1,16):
    square_dict[number] = number ** 2

square_dict

#1. Create a Set
my_set = {1, 2, 3, 3, 4}
print(my_set)

#2. Iterate Over a Set
#Write a Python program to iterate over sets.
fruits_set = {"apple", "banana", "pineapple", "cherry"}

for x in fruits_set:
  print(x)

#3. Add Member(s) to a Set
#Write a Python program to add member(s) to a set.
fruits_set = {"apple", "banana", "pineapple", "cherry"}
fruits_set.add("grapes")
fruits_set

#4. Remove Item(s) from a Set
#Write a Python program to remove item(s) from a given set.

fruits_set = {"apple", "banana", "pineapple", "cherry"}
fruits_set.remove("pineapple")
fruits_set

#5. Remove an Item if Present in the Set
#Write a Python program to remove an item from a set if it is present in the set.
fruits_set = {"apple", "banana", "pineapple", "cherry"}

if "cherry" in fruits_set:
    fruits_set.remove("cherry")   # elementni o'chirish
    print("Removed 'cherry' from set.")
else:
    print("'cherry' not found in the set.")

print(fruits_set)
