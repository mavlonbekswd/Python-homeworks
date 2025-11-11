#1. Create and Access List Elements
#Create a list containing five different fruits and print the third fruit.
fruits = ["apple", "banana", "pineapple", "grapes", "orange"]
fruits[2]

#2. Concatenate Two Lists
# Create two lists
list1 = [1, 2, 3, 4]
list2 = [5, 6, 7, 8]

# Concatenate the two lists
combined_list = list1 + list2

# Print the result
print("Concatenated list:", combined_list)



#. 3 Extract Elements from a List
theNumbers= [1,3,4,5,6,8,2]
first = theNumbers[0]
last = theNumbers[-1]
middle = theNumbers[len(theNumbers) // 2]
newList = first, middle, last
newList

##4. Convert List to Tuple
#Create a list of your five favorite movies and convert it into a tuple.

movies = ["Tundan_Tongacha","Poyqadam","Panox","Erkatoy", "Dada"]
convert = tuple (movies)
convert

#5. Check Element in a List
#Given a list of cities, check if "Paris" is in the list and print the result.

cites = ["Oslo", "London", "Madrid", "Paris"]
if "Paris" in cites:
 print("bor")
else: print ("yo'q")

## NOT IN = yo'qligini tekshirish

#7. Swap First and Last Elements of a List 
numbers = [10, 20, 30, 40, 50]

# Swap the first and last elements
numbers[0], numbers[-1] = numbers[-1], numbers[0]

# Print the result
print("List after swapping:", numbers)

#6. Duplicate a List Without Using Loops
#Create a list of numbers and duplicate it without using loops.
Numbers= [1,3,4,5,6,8,2]
copy = Numbers.copy()
copy

#8 Slicing
number = [1,2,3,4,5,6,7,8,9,10]
slice = number[3:7]
slice

#9. Count Occurrences in a List
#Create a list of colors and count how many times "blue" appears in the list.
colors= ["blues", "green", "navy", "grey","blues", "green", "white", "black" "blues","green", "white", "black" , "blues"]

count = colors.count("blues")
count

#10. Find the Index of an Element in a Tuple
#Given a tuple of animals, find the index of "lion".

animals = ("tiger", "zebra", "snake", "lion", "owl")
index = animals.index("lion")
index


#11. Merge Two Tuples
#Create two tuples of numbers and merge them into a single tuple.
number1 = (1,2,3,4,5,6,7,8,9,10)
number2 = (1,2,3,4,5,6,7,8,9,10)

marge = number1 + number2
marge

#12. Find the Length of a List and Tuple
#Given a list and a tuple, find and print their lengths.

number1 = [1,2,3,4,5,6,7,8,9,10]
number2 = (1,2,3,4,5,6,7,8,9,11,12)

lenlist1 = len(number1)
lenlist2 = len(number2)
lenlist1, lenlist2


#13. Convert Tuple to List
#Create a tuple of five numbers and convert it into a list.

number2 = (1,2,3,4,5,6,7,8,9,11,12)
listnumber = list(number2)
listnumber

#14. Find Maximum and Minimum in a Tuple
#Given a tuple of numbers, find and print the maximum and minimum values.

number2 = (1,2,3,4,5,6,7,8,9,11,12)

maxval= min(number2)
minval= max(number2)
maxval, minval

#15. Reverse a Tuple
#Create a tuple of words and print it in reverse order.

words = ("m", "n", "o", "p")

words_list = list(words)   # bu endi to‘g‘ri ishlaydi
words_list.reverse()

reversed_tuple = tuple(words_list)
print(reversed_tuple)
