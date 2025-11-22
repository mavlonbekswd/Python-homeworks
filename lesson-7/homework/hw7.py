✅ 1. is_prime(n) Function
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

# Examples
print(is_prime(4))  # False
print(is_prime(7))  # True

🔹 Example with filter():

Find all prime numbers from a list:

nums = [2, 3, 4, 5, 6, 7, 8, 9, 10]
primes = list(filter(is_prime, nums))
print(primes)  # [2, 3, 5, 7]

✅ 2. digit_sum(k) Function
def digit_sum(k):
    return sum(map(int, str(k)))

# Examples
print(digit_sum(24))   # 6
print(digit_sum(502))  # 7

🔹 Example with map():
numbers = [24, 502, 1234]
result = list(map(digit_sum, numbers))
print(result)  # [6, 7, 10]

✅ 3. Powers of Two Function
def powers_of_two(N):
    num = 2
    while num <= N:
        print(num, end=" ")
        num *= 2

# Example
powers_of_two(10)  # 2 4 8

🔹 Example using filter() + map():
nums = range(1, 50)
powers = list(filter(lambda x: x & (x - 1) == 0 and x != 0, nums))
print(powers)  # [1, 2, 4, 8, 16, 32]
